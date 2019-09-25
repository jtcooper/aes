from ctypes import c_uint8


def ffAdd(b1, b2):
    return b1 ^ b2


def ffMultiply(b1, b2):
    added_bytes = []
    x = b1

    i = 0
    while i < 8:  # 8 is the number of bits in a byte
        # get the bit associated with the current xtimes operation and see if we need to include it
        if bit(b2, i) == 1:
            added_bytes.append(x)
        x = xtime(x)
        i = i + 1

    # add the saved byte values together
    result = 0
    for byte in added_bytes:
        result = result ^ byte
    return result


def xtime(x: int) -> int:
    msb = bit(x, 7)
    result = x << 1
    if msb == 1:
        result = result ^ 0x1b
    # convert to uint8 to chop off extra bit
    return c_uint8(result).value


# return ith bit of byte
def bit(byte: int, i: int) -> int:
    mask = (0x01 << i)
    return (byte & mask) >> i
