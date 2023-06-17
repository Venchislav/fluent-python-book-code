# dict has value() method, that shows values 
d = dict(a=10, b=20, c=30)
values = d.values()
print(values)

# we can also

print(len(values))

# But we can't show exact element by index constr
# print(values[0])

# We can also add some elems

d['z'] = 99
print(d)

print(values)