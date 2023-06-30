# cache saves the result of function

from gigadecorators import clock
import functools

# It's kinda bad code
# As it calls func with the same args
"""
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
    
"""

# decorators composition works as
# @functools.cache
# @clock
# =
# fibonacci = functools.cache(clock(fibonacci()))
# It means that we use clock() first and then cache


@functools.cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
