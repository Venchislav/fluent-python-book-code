charles = {'name': 'Charles L. Dodgson', 'born': 1982}

lewis = charles
print(lewis is charles)

print(id(lewis), id(charles))

lewis['balance'] = 950

print(charles)


alex = {'name': 'Charles L. Dodgson', 'born': 1982, 'balance': 950}

print(alex == charles)
print(alex is not charles)


# WTH
# The thing is: var alex is a link to the object (dict)
# Which is the same to the object, that was assigned to the charles var
# And in assigning these object become equal, because of __eq__ method
# But these are different objects (we can see it with is not)

print(id(alex), id(charles))  # IDs are not the same


# So:
# '==' - compares values of objects (their data inside)
# 'is' - compares IDs of objects

# We use is to singletons values: None etc.
# And also is works faster than '==' and it can't be overloaded

# But mostly coders use '==' (excepting None singleton)
