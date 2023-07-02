def console_writer(info):
    print(info)


def file_writer(info):
    with open('x.txt', 'a') as file:
        file.write(info + '\n')


def client(writer):
    writer('Hello world!')
    writer('See ya!')


if input('Write file? [Y/N]') == 'Y':
    client(file_writer)
else:
    client(console_writer)
