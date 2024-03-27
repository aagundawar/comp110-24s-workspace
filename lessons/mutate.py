"""Mutating functions."""

__author__ = "730663390"


def manual_append(lst: list[int], number: int) -> None:
    """Appends a given integer to the end of the list."""
    lst.append(number)


def double(lst: list[int]) -> None:
    """Mutates list by multiplying each value in the list by 2."""
    i: int = 0
    while i < len(lst):
        lst[i] *= 2
        i += 1