b = 3


def f1(a):
    print(a)
    print(b)

# Wrong as code prefers to use local vars first
# But here we use it before assignment

# def f2(a):
#     print(a)
#     print(b)
#     b = 2


print(f1(3))
# print(f2(3))


# but we can change f2:
def f2(a):
    global b
    print(a)
    print(b)
    b = 9


print(f2(3))
