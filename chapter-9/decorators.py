# decorator is a callable obj that gets another func as an arg

def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


# inner is called
target()

print(target)
