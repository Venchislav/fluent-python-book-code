from functools import reduce
from operator import add, mul


# map and filter nowadays are pretty useless
# we can use arr generator instead


def factorial(n):
    """ returns n!"""
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


print(list(map(factorial, range(6))))
print([factorial(i) for i in range(6)])

print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])

# There's no need in reduce too
# As minimum as it's not included to standard python

print(reduce(add, range(6)))
print(sum(range(6)))


# But reduce is not that bad!

def factorial(n):
    return reduce(mul, range(1, n + 1))


var = lambda n: reduce(mul, range(1, n + 1))
print(var(5))
