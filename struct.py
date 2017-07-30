from struct import *

packed_data = pack('iis', 6,6,'s')
print(packed_data)

print(calcsize('i'))
print(calcsize('i'))
print(calcsize('s'))

unpacked_data=unpack('iis', packed_data)
print(unpacked_data)