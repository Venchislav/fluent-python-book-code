# Here's an example of closure


def make_averager():
    series = []

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return average


avg = make_averager()
avg(10)
print(avg(11))
print(avg(15))

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
# series value is in __closure__ attr
print(avg.__closure__[0].cell_contents)


# the following code below doesn't work
# As inner var tries to use its own local vars, which are not assigned

"""
def make_averager():
    count = 0
    total = 0
    
    def averager(new_value):
        count += 1
        total += new_value
        return total / count
        return averager
"""

# to avoid this sh*t we have to use nonlocal before vars usage

# This is an optimized and appropriately working function
# As it doesn't make that calculations for every element


def make_averager2():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return average


avg = make_averager2()
avg(10)
print(avg(11))
print(avg(15))
