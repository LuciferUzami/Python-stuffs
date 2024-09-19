from random import *
from typing import Tuple


def colors() -> Tuple[int, int, int]:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b
