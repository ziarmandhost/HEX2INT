def hex2le(val):
    little_hex = bytearray.fromhex(val[2:])
    little_hex.reverse()
    return int.from_bytes(little_hex, "big")


def hex2be(hex_str):
    return int(hex_str, 16)


def le2hex(le_num, bytes_num):
    le_bytes = le_num.to_bytes(bytes_num, "little")
    return "0x" + le_bytes.hex()


def be2hex(be_num, bytes_num):
    be_bytes = be_num.to_bytes(bytes_num, "big")
    return "0x" + be_bytes.hex()
