from typing import TypeVar


T = TypeVar("T", int, float, str)


def add(a: T, b: T) -> T:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError
    return a / b
