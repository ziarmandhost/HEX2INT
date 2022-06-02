from lib import hex2le, hex2be, le2hex, be2hex

# HEX -> LE or BE
vector_value = str(input("Type value of the vector: "))

print("HEX -> Little Endian: ", hex2le(vector_value))
print("HEX -> Big Endian: ", hex2be(vector_value))

# LE -> HEX
little_endian = int(input("Type Little Endian value (int): "))
le_bytes_num = int(input("Type bytes number (int): "))
print("Little Endian -> HEX: ", le2hex(little_endian, le_bytes_num))

# BE -> HEX
big_endian = int(input("Type Big Endian value (int): "))
be_bytes_num = int(input("Type bytes number (int): "))
print("Big Endian -> HEX: ", be2hex(big_endian, be_bytes_num))
