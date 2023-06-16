# Sorted creates a new arr or other iterable object

x = [4, 2, 87, 1, 8]

y = sorted(x)
print(id(x), id(y))

x = [2, 1, 3, 5]
x.sort()
print(x)
# function and method also have 2 unnecessary args:
# 1) reversed=True - It will be sorted from higher to lower
# By default it's false (thancks god)
# 2) key=smth - Conition of sorting
# ex. key=len - sorts elems by their len

a = ['Hi', 'Hello', 'Hey']
print(sorted(a, key=len))

# And that's how key can work

l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]

# This way it will consider str elems with digits as int digits!
print(sorted(l, key=int))
