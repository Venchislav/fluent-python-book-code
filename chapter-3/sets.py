from unicodedata import name

# set is a SET of unique elems
l = ['spam', 'spam', 'eggs', 'spam' , 'bacon']
print(set(l))

print(dict.fromkeys(l).keys())

print(list(dict.fromkeys(l).keys()))


s = {1}
print(type(s))

print(s.pop())


a = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(a)

d1 = {'a', 'd', 'g'}
s = {'a', 'b', 'c'}

# cross of 2 sets (same elems)
print(d1 & s)