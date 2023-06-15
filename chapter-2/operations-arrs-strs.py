l = [1, 2, 3, 4, 5]
print(l*5)

l = 'abcde'
print(l*2)

# 3 sub arrays with 3 empty elements
board = [['_'] * 3 for i in range(3)]
print(board)
board[0][2] = 'x'
print(board)

print('----------')

l = [1, 2, 3]
print(id(l)) # Same

l *= 2
print(id(l)) # Same
# That means that l still being the only object
print('----------')

t = (1, 2, 3)
print(id(t)) # Not same

t *= 2
print(id(t)) # Not same
# That means that tuple creates a new object here

# Just with no context...
# There's a cool method extend() for arrs in python

t = (1, 2, [30, 40])
t[2].extend([50, 60])
print(t)
# IDK why I wrote about it. Just for the fact...
# And also += won't really work here
# P.S Actually it's not a good deal to use changeble structures in not changeble
