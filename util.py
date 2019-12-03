from typing import Callable


def get_input(loc, func: Callable = str, strip=True):
    with open(loc) as data:
        return [func(line.strip() if strip else line) for line in data]
