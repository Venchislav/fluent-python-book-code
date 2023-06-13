"""
Vector: A simplified class that demonstrates some special methods.
Simplified for didactic reasons. The class lacks the correct
error handling, especially in the ``__add__`` and ``__mul__`` methods.
This example will be expanded upon substantially later in the book.
Addition::
>> v1 = Vector(2, 4)
>> v2 = Vector(2, 1)
>> v1 + v2
Vector(4, 5)
Absolute value::
>> v = Vector(3, 4)
>> abs(v)
5.0
Multiplication by a scalar::
>> v * 3
Vector(9, 12)
>> abs(v * 3)
15.0
"""

import math
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Just for beauty
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    # Here we use hypotenuse formula
    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        # if abs(self) == 0 - False. If not - True
        # return bool(abs(self)) - Good, but not enough
        return bool(self.x or self.y)
        # Here we don't use abs().

    # Sum two vectors
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # Multiply vector on scalar
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(x=6, y=9)
print(bool(v1))