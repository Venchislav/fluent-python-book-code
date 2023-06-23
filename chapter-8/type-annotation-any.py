# Type annotations can use every nearly every type
# But there are some rules
from typing import Any


# Type Any - means any :) supports every operation

def double(x):
    return x * 2


# =


def double(x: Any) -> Any:
    return x * 2


# object seems to be the same to Any
# But it doesn't support __mul__
# It will work, but it's not that good: even MyPy will regret it and consider it as an error


# def double(x: object) -> object:
#     return x * 2


