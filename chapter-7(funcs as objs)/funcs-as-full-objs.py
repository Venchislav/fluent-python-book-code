# python funcs are full objects because:

# They can be created while program is working
# It can be assigned to the var or datastructure field
# It can be assigned as a function arg
# May be returned as a result in function

# ints strs arrs and more are also full objects

# Work with func as with object

def factorial(n):
    """ returns n!"""
    if n <= 1:
        return 1
    else:
        return factorial(n-1)*n


print(factorial(5))
print(factorial.__doc__)
print(type(factorial))

# Function in python is an object too
