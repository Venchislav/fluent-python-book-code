from typing import NamedTuple


class DemoNTClass(NamedTuple):
    a: int
    b: float
    c = 'spam'


# Here we can see annotations and vars they've been used by
print(DemoNTClass.__annotations__)
