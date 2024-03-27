"""EX05 - Dictionary Utils Tests."""

__author__ = "730663390"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


# Function 1: invert
def test_invert_duplicate_values():
    """Tests inverting a dictionary with duplicate values raises a KeyError(edge)."""
    with pytest.raises(KeyError):
        my_dictionary: dict[str, str] = {"alyssa": "byrnes", "adam": "byrnes"}
        invert(my_dictionary)


def test_invert_single_pair():
    """A dictionary with a single key-value pair gets inverted."""
    my_dictionary: dict[str, str] = {"a": "b"}
    assert invert(my_dictionary) == {"b": "a"}


def test_invert_multiple_pairs():
    """A dictionary with multiple key-value pairs should invert each pair while maintaining the pairs."""
    my_dictionary: dict[str, str] = {"a": "b", "c": "d", "e": "f", "g": "h"}
    assert invert(my_dictionary) == {"b": "a", "d": "c", "f": "e", "h": "g"}


# Function 2: favorite_color
def test_favorite_color_empty():
    """An empty dictionary will return nothing as the favorite color(edge)."""
    my_dictionary: dict[str, str] = {}
    assert favorite_color(my_dictionary) == ""


def test_favorite_color_single_pair():
    """A dictionary with a single key-value pair will return the value as the favorite color."""
    my_dictionary: dict[str, str] = {"Alice": "blue"}
    assert favorite_color(my_dictionary) == "blue"


def test_favorite_color_tie():
    """A dictionary with a tie for favorite color will return the color that appears in the dictionary first."""
    my_dictionary: dict[str, str] = {"Alice": "blue", "Marc": "yellow", "Ezri": "blue", "Kris": "yellow"}
    assert favorite_color(my_dictionary) == "blue"


# Function 3: count
def test_count_empty():
    """An empty list will return an empty dictionary as the result(edge)."""
    my_list: list[str] = []
    assert count(my_list) == {}


def test_count_single_value():
    """A list with a single value will return the value 1."""
    my_list: list[str] = ["a"]
    assert count(my_list) == {"a": 1}


def test_count_multiple_values():
    """A list with a multiple values will return a dict with the frequency of each unique key."""
    my_list: list[str] = ["apple", "banana", "apple", "orange"]
    assert count(my_list) == {"apple": 2, "banana": 1, "orange": 1}


# Function 4: alphabetizer
def test_alphabetizer_empty():
    """An empty list will return an empty dictionary as the result(edge)."""
    my_list: list[str] = []
    assert alphabetizer(my_list) == {}


def test_alphabetizer_single_value():
    """A list with a single value will return the value with it's first leter."""
    my_list: list[str] = ["apple"]
    assert alphabetizer(my_list) == {"a": "apple"}


def test_alphabetizer_multiple_values():
    """A list with a multiple values will return a dict with a unique letter and each word associated with it."""
    my_list: list[str] = ["apple", "boy", "cat", "ant", "bread"]
    assert alphabetizer(my_list) == {"a": ["apple", "ant"], "b": ["boy", "bread"], "c": ["cat"]}


# Function 5: update_attendance
def test_update_attendance_empty():
    """An empty string will return an empty string in the dictionary as the result(edge)."""
    my_dictionary: dict[str, str] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day_of_the_week = ""
    student_name = ""
    assert update_attendance(my_dictionary, day_of_the_week, student_name) == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "": [""]}


def test_update_attendance_existing_day():
    """Given a day that is already in the dictionary, updating the attendance with a new student will add it to the corresponding day in the dictionary."""
    my_dictionary: dict[str, str] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day_of_the_week = "Monday"
    student_name = "Johnny"
    assert update_attendance(my_dictionary, day_of_the_week, student_name) == {"Monday": ["Vrinda", "Kaleb", "Johnny"], "Tuesday": ["Alyssa"]}


def test_update_attendance_new_day():
    """Given a day that isn't already in the dictionary, updating the attendance with a new student will add it to a new day in the dictionary."""
    my_dictionary: dict[str, str] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day_of_the_week = "Wednesday"
    student_name = "Alexander"
    assert update_attendance(my_dictionary, day_of_the_week, student_name) == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": ["Alexander"]}