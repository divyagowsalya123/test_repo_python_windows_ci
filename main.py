import math
from typing import Union
def add(a: Union[int, float], b: Union[int, float]) -> int:
    return math.floor(a + b)


def to_sentence(s: str) -> str:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'
