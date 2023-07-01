class Bird:

    def feed(self) -> None:
        print("Feeding the dude")


class Duck(Bird):
    def feed(self) -> None:
        print("Feeding the duck...")


class Goose:
    """
    This class is not a child of Bird class
    """
    def feed(self) -> None:
        print("Feeding the goose...")


# We use typehint
def feed(bird: Bird) -> None:
    bird.feed()


# OK
feed(Bird())

# OK
feed(Duck())

# Mypy error: Argument 1 to "feed" has incompatible type "Goose";
#  expected "Bird"
# So as we use typehint of Bird, Goose will cause an error, as it's not a child of Bird
feed(Goose())

# Nominal typing is about class names etc.
