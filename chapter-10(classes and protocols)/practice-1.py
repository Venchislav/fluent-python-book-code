# This is just a file with no context, I just decided to practice a bit in OOP

import numpy as np
import builtins

# namespace in library
for name in np.__dict__:
    print(name)


class Doges:

    def __init__(self, dog):
        self.name = dog

    def __str__(self):
        return f'{self.name} is cool'

    def __repr__(self):
        return f'Dogo(\'{self.name}\')'


c = Doges('Flipper')
print(c.__dict__)
print(str(c))
print(repr(c))

print(builtins.abs(-155))

# Description (instruction) how to use tool and what does it make
# WTH I didn't know it for the years!💀
print(help(builtins.abs))


def student(student_id, student_name, student_class):
    return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'


print(student('S122', 'Wilson Medina', 'VI'))


def func_that_shows_arg_names(x, y, z):
    # shows arg_names_of_func
    return func_that_shows_arg_names.__code__.co_varnames


print(func_that_shows_arg_names(1, 2, 3))
print(student.__code__.co_varnames)
