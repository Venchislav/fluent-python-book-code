# Higher order function is a function that gets func as an arg
# or return it as a value

fruits = ['strawberry',
          'fig',
          'apple',
          'cherry',
          'raspberry',
          'banana']

# key here is kwarg for sorted func
# And it gets another func (len) as an argument
print(sorted(fruits, key=len))
# The same thing is about print. It also gets funcs as args sometimes

