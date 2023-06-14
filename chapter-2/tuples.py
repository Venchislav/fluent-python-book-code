a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(a == b)
b[-1].append(3)
print(a == b)

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])
# And it will work because only fixed types are hashable

# True False
print(fixed(tf), fixed(tm))

# And it's an easy way of unzipping tuples
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)

# Damn son...
a, b, *rest = range(5)
print(a, b, rest) # 0 1 [2, 3, 4]

a, b, *rest = range(2)
print(a, b, rest) # 0 1 []

# We can also use * (unzip) multiple times

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

print((fun(*[1, 2], 3, *range(4, 7))))

# It can be used nearly evwrywhere!

print(*range(9), 9)




metro_areas = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon  <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
if __name__ == '__main__':
    main()