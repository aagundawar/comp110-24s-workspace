"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    n = len(x)
    sorted_index = 0
    while sorted_index < n - 1:
        unsorted_index = sorted_index + 1
        while unsorted_index > 0 and x[unsorted_index] < x[unsorted_index - 1]:
            temp = x[unsorted_index]
            x[unsorted_index] = x[unsorted_index - 1]
            x[unsorted_index - 1] = temp
            unsorted_index -= 1
        sorted_index += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    n = len(x)
    for i in range(n - 1):
        min_index = i
        for y in range(n):
            if y > i and x[y] < x[min_index]:
                min_index = y
        if min_index != i:
            temp_list = x[i]
            x[i] = x[min_index]
            x[min_index] = temp_list
    return None
    