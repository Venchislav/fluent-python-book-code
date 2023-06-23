from typing import Union

# union is similar to | (means or)

# returns str or float here


def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token


def tokenize(text: str) -> list[str]:
    return text.upper().split()

