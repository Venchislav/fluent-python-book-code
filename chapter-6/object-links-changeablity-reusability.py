# An easy example of the fact that vars
# are not the objects themselves

# a = [1, 2, 3, 4, 5]
# b = a
#
# a.append(6)
# print(b)

class Gizmo:
    def __init__(self):
        print(f'Gizmo id: {id(self)}')


x = Gizmo()

