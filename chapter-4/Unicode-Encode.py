city = 'São Paulo'
print(city.encode('utf8'))

print(city.encode('utf16'))

print(city.encode('iso8859_1'))

# city.encode('cp437') - causes UnicodeEncodeError

# To ignore these we don't even have to write try except

print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))