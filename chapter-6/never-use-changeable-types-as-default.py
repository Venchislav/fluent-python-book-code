class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus = HauntedBus(['Alice', 'Bob'])
print(bus.passengers)
bus.pick('Charlie')
print(bus.passengers)
bus.drop('Bob')
print(bus.passengers)

bus2 = HauntedBus()
bus2.pick('Carry')
print(bus2.passengers)

bus3 = HauntedBus()
print(bus3.passengers)

# The problem is that bus2 and bus3 link to the same default arr
# So we should never use changeable types as default
# Even PyCharm says it!
# Better use None
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)
print(HauntedBus.__init__.__defaults__[0] is bus.passengers)
