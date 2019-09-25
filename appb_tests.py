from cipher import cipher
from inv_cipher import inv_cipher
from key_expansion import key_expansion
from util import getw
from operations import ffAdd, xtime, ffMultiply
from globals import Nb
import numpy as np

# finite field arithmetic unit tests
assert ffAdd(0x57, 0x83) == 0xd4
assert xtime(0x57) == 0xae
assert xtime(0xae) == 0x47
assert xtime(0x47) == 0x8e
assert xtime(0x8e) == 0x07
assert ffMultiply(0x57, 0x13) == 0xfe

# test cipher
Nk = 4
Nr = 10
input_bytes = bytearray([0x32, 0x88, 0x31, 0xe0, 0x43, 0x5a, 0x31, 0x37,
                         0xf6, 0x30, 0x98, 0x07, 0xa8, 0x8d, 0xa2, 0x34])
cipher_key = bytearray([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
                        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])
expected = bytearray([0x39, 0x02, 0xdc, 0x19, 0x25, 0xdc, 0x11, 0x6a,
                      0x84, 0x09, 0x85, 0x0b, 0x1d, 0xfb, 0x97, 0x32])
w = getw(Nb, Nr)
key_expansion(cipher_key, w, Nk, Nr)
out = cipher(input_bytes, w, Nr)
# print_bytes(out)
assert out == expected

# a randomly generated message should encrypt -> decrypt to the same thing
Nk = 6
Nr = 12
input_bytes = bytearray([np.random.randint(256) for i in range(16)])
cipher_key = bytearray([np.random.randint(256) for i in range(24)])
expected = input_bytes.copy()
w = getw(Nb, Nr)
key_expansion(cipher_key, w, Nk, Nr)
cipher_text = cipher(input_bytes, w, Nr)
out = inv_cipher(cipher_text, w, Nr)
assert out == expected
