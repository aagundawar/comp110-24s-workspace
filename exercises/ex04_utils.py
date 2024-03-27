"""EX04 - List Utility Functions!"""
 
__author__ = "730663390"


def all(input: list[int], num: int) -> bool:
    """Checks whether the list inputted matches the integer inputted."""
    if len(input) == 0:
        return False
    idx = 0
    while idx < len(input):
        if input[idx] != num:
            return False
        idx += 1
    return True


def max(input: list[int]) -> int:
    """Finds the maximum value in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest = input[0]
    idx = 0
    while idx < len(input):
        if input[idx] > largest:
            largest = input[idx]
        idx += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines whether each value in the first list is equal to each value in the second list."""
    if len(list1) != len(list2):
        return False
    i = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Puts the second list at the end of the first list."""
    i = 0
    while i < len(list2):
        list1.append(list2[i])
        i += 1
