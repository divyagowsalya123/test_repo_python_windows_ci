import math


def add(a: float, b: float) -> int:
    return math.floor(a + b)


def to_sentence(s: str) -> str:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'
