"""Unit tests for ex05 utils functions."""

__author__ = "730486771"

from exercises.ex05.utils import only_evens, sub, concat


# only_evens tests


def test_only_odd_numbers() -> None:
    """Checks that only_evens returns a blank list if all numbers in the inputted list are odd."""
    test_list: list[int] = [1, 3, 5, 7]
    assert only_evens(test_list) == []


def test_many_odds_and_evens() -> None:
    """Checks that only evens returns just even numbers when given a list of a mix of multiple odd and even numbers."""
    test_list: list[int] = [1, 4, 7, 6, 8, 9]
    assert only_evens(test_list) == [4, 6, 8]


def test_with_negative_evens() -> None:
    """Checks that only_evens will recognize and return negative numbers that are even."""
    test_list: list[int] = [-2, 4, 5, -6, -7]
    assert only_evens(test_list) == [-2, 4, -6]


# concat tests


def test_one_list_empty() -> None:
    """Checks that concat will still return correct numbers when one of the given lists is empty."""
    test_list1: list[int] = []
    test_list2: list[int] = [1, 5, 6]
    assert concat(test_list1, test_list2) == [1, 5, 6]


def test_list_one_element() -> None:
    """Checks that concat will concatenate the lists correctly if one of the lists only has one element."""
    test_list1: list[int] = [2, -8, 2]
    test_list2: list[int] = [-16]
    assert concat(test_list1, test_list2) == [2, -8, 2, -16]


def test_different_length_lists() -> None:
    """Checks if concat will return the correct list if the lengths of the given lists are different lengths."""
    test_list1: list[int] = [3, -4, -5]
    test_list2: list[int] = [6, 0, 8, -9, 30, 2]
    assert concat(test_list1, test_list2) == [3, -4, -5, 6, 0, 8, -9, 30, 2]


# sub tests


def test_a_list_empty() -> None:
    """Checks that sub will return an empty list if the inputted list is empty, even if start and end indexes are still given."""
    test_list: list[int] = []
    test_start: int = 1
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == []


def test_list_many() -> None:
    """Checks that given a list of many elements that sub will return the values from that list in the range between the given start and end indexes."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    test_start: int = 0
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == [1, 2, 3]


def test_list_with_negatives() -> None:
    """Checks if sub will still return the values in the given index range with negative values in the list."""
    test_list: list[int] = [-1, -4, 5, 7]
    test_start: int = 1
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == [-4, 5]