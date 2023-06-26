# def make_averager():
#     count = 0
#     total = 0
#
#     def averager(new_value):
#         count += 1
#         total += new_value
#         return  total / count
#
#     return averager
#
# avg = make_averager()
# avg(10)

# The code above is terribly bad, as averager func uses count and total as its local vars
# But they're not assigned, so it causes an error
# To solve it we have to use nonlocal

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
