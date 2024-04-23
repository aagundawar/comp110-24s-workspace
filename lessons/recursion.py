"""CQ07 - Recursions."""


__author__ = "730663390"


def f(n: int, k: int) -> int: 
    """Defines a function while using base case and recursive rule."""
    if n == 0:
        return 0
    else:
        return f(n - 1, k) + k
    