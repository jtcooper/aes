from typing import List

import numpy as np

from globals import Nb


def transpose(b: bytearray, nb: int = Nb) -> bytearray:
    # convert to matrix
    t = np.matrix([b[i*nb:i*nb+nb] for i in range(int(len(b) / 4))])
    t = np.matrix.transpose(t)
    return bytearray(t.flatten().tolist()[0])


# test
test = bytearray([0x00, 0x11, 0x22, 0x33,
                  0x44, 0x55, 0x66, 0x77,
                  0x88, 0x99, 0xaa, 0xbb,
                  0xcc, 0xdd, 0xee, 0xff])
step1 = transpose(test)
assert step1 != test
out = transpose(step1)
assert test == out


def bytearray_to_str(b: bytearray) -> str:
    return ''.join(["{:02x}".format(i) for i in b])


def debug_get_round(round: int) -> str:
    return "round[{:2d}].".format(round)


def print_debug(key: str, value: str):
    print("{:19s}".format(key) + value)


def print_bytes(b: bytearray):
    s = ['0x%02x' % byte for byte in b]
    print(s)
    return s


def matrix_element(matrix: bytearray, col: int, row: int, row_width: int = Nb) -> int:
    return matrix[matrix_index(col, row, row_width)]


def matrix_index(col: int, row: int, row_width: int = Nb) -> int:
    return row * row_width + col


def getw(nb: int, nr: int) -> List:
    return [None] * (nb * (nr + 1))


def block_bytes(key: List[bytearray], rotate=True) -> List[bytearray]:
    result = []
    if rotate:
        for i in range(int(len(key) / 4)):
            b = bytearray(16)
            for j in range(0, 4):
                b[j] = key[i*4+j][0]
                b[j+4] = key[i*4+j][1]
                b[j+8] = key[i*4+j][2]
                b[j+12] = key[i*4+j][3]
            result.append(b)
        return result
    else:
        for i in range(int(len(key) / 4)):
            b = bytearray(16)
            for j in range(0, 4):
                b[j*4:j*4+4] = key[i*4+j][0:4]
            result.append(b)
        return result


def int_to_bytes(i: int) -> bytearray:
    return bytearray.fromhex('{:08x}'.format(i))


def bytes_to_int(b: bytearray) -> int:
    return int.from_bytes(b, 'big')


def print_head(plaintext: bytearray, key: bytearray):
    print("\n")
    print_debug("PLAINTEXT:", bytearray_to_str(plaintext))
    print_debug("KEY:", bytearray_to_str(key))
    print()
