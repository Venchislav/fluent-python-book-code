# It's the simplest showcase of match case
# Cases can also be written as:

# case 'top' | 'left' | 'down':
#   print('left top or down')

"""
cmd = 'right'

match cmd:
    case 'top':
        print('Вверх')

    case 'left':
        print('Влево')

    case 'domwn':
        print('Вниз')

    case 'right':
        print('Вправо')

    # Else
    case _:
        print('Другое')
"""

# But it's better than C++ or even Java because:

cmd = 'right'

match cmd:
    # command = cmd
    # But this block always on
    case command:
        print(f'Command {command}') # Command right

# But we can refactor it:

match cmd:
    # If
    case 'top':
        print('top')
    # Else
    case command:
        print(f'Command {command}') # Command right


# We can also handle it by type:
# But bool() doesn't work by default

cmd = 23
match cmd:
    case str():
        print("Oh! It's a string")
    case int():
        print("Oh! It's an int")

# bool() type fix:

cmd = True
match cmd:
    case bool():
        print("OOOh!!! It's bool")
    case str():
        print("Oh! It's a string")
    case int():
        print("Oh! It's an int")

# It just should be before int()

# But it's not it...

cmd = 'pepe'
match cmd:
    # command = cmd
    # It can be also written as:
    # case str(command) - But it's worse practice
    case str() as command:
        print(f"Oh! {command} is a string")
    case int():
        print("Oh! It's an int")

# We can also have if with case:


cmd = 90
match cmd:
    case str() as command:
        print(f"Oh! {command} is a string")

    # int case will only work with cmd > 50
    case int() as command if command > 50:
        print("Oh! It's an int")

    case _:
        print('Something else')