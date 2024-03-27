"""EX05 - Dictionary Utils."""

__author__ = "730663390"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values of a given dictionary."""
    inverted_dict = {}
    for key in input_dict:
        value = input_dict[key]
        if value in inverted_dict:
            raise KeyError("Duplicate value encountered.")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Prints out the color that is most frequent in the dictionary."""
    counter_dict: dict[str, int] = {}
    top_color: str = ""
    max: int = 0
    for key in input_dict:
        if input_dict[key] in counter_dict:
            counter_dict[input_dict[key]] += 1
        else:
            counter_dict[input_dict[key]] = 1
    for i in counter_dict:
        if counter_dict[i] > max:
            max = counter_dict[i]
            top_color = i
    return top_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the frequency of each unique item in a list."""
    freq_dict: dict[str, int] = {}
    for elem in input_list:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1
    return freq_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Categorizes all items in the list by their first letter."""
    alphabet_dict: dict[str, list[str]] = {}
    for word in input_list:
        first_letter: str = word[0].lower()
        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(word)
        else:
            alphabet_dict[first_letter] = [word]
    return alphabet_dict


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance log for a specific day and student."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]