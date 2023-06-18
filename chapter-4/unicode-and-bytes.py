s = 'café'
print(len(s))
# encoding
# UTF-8 converts str to bytes
b = s.encode('utf8')
print(b)
print(len(b))
# decoding
b = b.decode('utf8')
print(len(b))

cafe = bytes('café', encoding='utf8')
print(cafe)
print(cafe[0])

print(cafe[:1])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

print('----------')

# Difference betwen codecs
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')