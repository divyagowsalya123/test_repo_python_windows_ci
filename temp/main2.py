import math
from typing import Union


def sub(a: Union[int, float], b: Union[int, float]) -> int:
    return math.floor(a - b)


def word_count(sentence: str, word: str) -> int:
    sentence_split = sentence.lower().split()

    if word in sentence_split:
        return sum([1 for x in sentence_split if x == word])
    else:
        return 0
