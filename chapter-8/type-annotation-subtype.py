class T1:
    pass


class T2(T1):
    pass


def f1(p: T1):
    return p


o2 = T2()
f1(o2)

# It's Liskov Substitution  usage poggers!
