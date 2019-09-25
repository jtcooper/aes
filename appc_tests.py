from util import getw, print_head
from globals import Nb
from inv_cipher import inv_cipher
from key_expansion import key_expansion
from cipher import cipher

# C1
Nk = 4
Nr = 10
plaintext = bytearray.fromhex('00112233445566778899aabbccddeeff')
key = bytearray.fromhex('000102030405060708090a0b0c0d0e0f')
print_head(plaintext, key)
w = getw(Nb, Nr)
key_expansion(key, w, Nk, Nr)
ciphertext = cipher(plaintext.copy(), w, Nr, debug=True)
out = inv_cipher(ciphertext, w, Nr, debug=True)
assert out == plaintext

# C2
Nk = 6
Nr = 12
key = bytearray.fromhex('000102030405060708090a0b0c0d0e0f1011121314151617')
print_head(plaintext, key)
w = getw(Nb, Nr)
key_expansion(key, w, Nk, Nr)
ciphertext = cipher(plaintext.copy(), w, Nr, debug=True)
out = inv_cipher(ciphertext, w, Nr, debug=True)
assert out == plaintext

# C3
Nk = 8
Nr = 14
key = bytearray.fromhex('000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f')
print_head(plaintext, key)
w = getw(Nb, Nr)
key_expansion(key, w, Nk, Nr)
ciphertext = cipher(plaintext.copy(), w, Nr, debug=True)
out = inv_cipher(ciphertext, w, Nr, debug=True)
assert out == plaintext
