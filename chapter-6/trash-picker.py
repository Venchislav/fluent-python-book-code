import weakref
a = [1, 2]
b = a
# We delete link to the obj
del a
# But we have another link, so object exists
print(b)

# Here we change link b
b = [5]
# That means that we lost the last link to the arr obj and it can be deleted

# Now we can see death of obj in realtime :(

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('...like tears in the rain.')


ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print(ender.alive)

s2 = 'spam'
print(ender.alive)
