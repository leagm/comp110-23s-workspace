"""Unit tests for EX07 functions."""

__author__ = "730486771"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest

# invert tests


# tests what happens if there are duplicate values in the input dictionary - Edge case


def test_check_key_error() -> None:
    """Tests what happens if there are duplicate values in the input dictionary."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


# tests that the length of the values and the keys in the dictionary does not affect them being inverted - Use case


def test_length_of_values_and_keys() -> None:
    """Tests that the length of the values and the keys in the dictionary does not affect them being inverted."""
    test_dict: dict[str, str] = {"t": "apple", "candycorn": "boo", "iiiitttsss": "supercalifragilisticexpialidocious"}
    assert invert(test_dict) == {"apple": "t", "boo": "candycorn", "supercalifragilisticexpialidocious": "iiiitttsss"}


# tests that the length of the dictionary itself does not affect it being inverted - Use case


def test_length_of_dict() -> None:
    """Tests that the length of the dictionary itself does not affect it being inverted."""
    test_dict: dict[str, str] = {"veryshort": "justonekeyvaluepair"}
    assert invert(test_dict) == {"justonekeyvaluepair": "veryshort"}


# favorite color tests


# tests that when an empty dictionary is entered, the code will not proceed. I added a message for fun - Edge case


def test_empty_dict() -> None:
    """Tests that when an empty dictionary is entered, the code will not proceed."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == "Enter a dictionary with values!"


# tests that when there is a tie for which color is the most frequent that the color which appears in the dictionary first is returned as the favorite color - Use case


def test_fav_color_tie_return_first_in_dict() -> None:
    """Tests that when there is a tie for which color is the most frequent that the color which appears in the dictionary first is returned as the favorite color."""
    test_dict: dict[str, str] = {"Marc": "green", "Steph": "purple", "Steve": "blue", "Rachel": "yellow", "Brad": "purple", "Daisy": "yellow"}
    assert favorite_color(test_dict) == "purple"


# tests that even if all values are the same, the code will just return that value as the favorite color - Use case


def test_one_color_only() -> None:
    """Tests that even if all values are the same, the code will just return that value as the favorite color."""
    test_dict: dict[str, str] = {"Stacy": "green", "Chase": "green", "Penny": "green"}
    assert favorite_color(test_dict) == "green"


# count tests


# tests that the code will not progress if an empty list is inputted. I added a message for fun - Edge case


def test_empty_list() -> None:
    """Tests that the code will not progress if an empty list is inputted."""
    test_list: list[str] = []
    assert count(test_list) == "Enter a list with values!"


# tests that when a duplicate value appears as the list is being iterated through that its value will increase in the resulting dictionary - Use case


def test_multiple_same_values() -> None:
    """Tests that when a duplicate value appears as the list is being iterated through that its value will increase in the resulting dictionary."""
    test_list: list[str] = ["apple", "cherry", "cherry", "banana"]
    assert count(test_list) == {"apple": 1, "cherry": 2, "banana": 1}


# tests that when a list only has one key-value pair that the kay will be added to the resulting dictionary and its value will equal one - Use case


def test_list_one_value() -> None:
    """Tests that when a list only has one key-value pair that the kay will be added to the resulting dictionary and its value will equal one."""
    test_list: list[str] = ["boop"]
    assert count(test_list) == {"boop": 1}