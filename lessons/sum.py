"""Summing the elements of a list using different loops!"""

__author__ = "730663390"


def w_sum(vals: list[float]) -> float:
    """Adds up all the values in the list of floats."""
    total = 0.0
    idx = 0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Adds up all the values in the list of floats."""
    total = 0.0
    for elem in vals:
        total += elem
    return total


def f_range_sum(vals: list[float]) -> float:
    """Adds up all the values in the list of floats."""
    total = 0.0
    for idx in range(0, len(vals)):
        total += vals[idx]
    return total