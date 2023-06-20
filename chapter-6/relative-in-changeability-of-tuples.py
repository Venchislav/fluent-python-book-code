# After change of changeable elem of tuple
# tuple also changes
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)  # True

t1[-1].append(50)
print(t1)

print(t1 == t2)  # False

# hash(t1) - is in-hashable

print('------------')

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)
