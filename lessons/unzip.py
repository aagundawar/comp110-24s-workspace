"""Splitting a dictionary into two lists."""

__author__ = "730663390"


def get_keys(input_dict: dict[str, int]) -> list[str]:
    """Takes each string value in the dictionary and compiles it into a seperate list."""
    keys: list[str] = []
    for key in input_dict:
        keys.append(key)
    return keys


def get_values(input_dict: dict[str, int]) -> list[int]:
    """Takes each integer value in the dictionary and compiles it into a seperate list."""
    values: list[int] = []
    for key in input_dict:
        values.append(input_dict[key])
    return values