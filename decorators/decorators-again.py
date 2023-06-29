# Yep, decorators again as I am dumbass and didn't understand
# them right

def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


target()
print(target)