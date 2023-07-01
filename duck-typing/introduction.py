# duck typing is a concept for dynamically typed langs
# it's about that we don't need to check obj type, but we have to check its methods

class Meter:
    def __len__(self):
        return 1_000


print(len(Meter()))

# Here is the main idea really. Len func doesn't really care about type of arg,
# it just checks if it's possible to use len for obj

