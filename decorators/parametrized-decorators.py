registry = set()


def register(active=True):
    def decorate(func):
        print('running register'
              f'(active={active}) -> decorate({func})')
        # register func only if active
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


f1()
f2()

print(registry)
