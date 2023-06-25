registry = []

# this func appends funcs with register decorator


def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


# main() is called only when file is ran as script
if __name__ == '__main__':
    main()
