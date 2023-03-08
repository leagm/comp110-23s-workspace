"""Unit tests for ex05 utils functions"""

__author__ = "730486771"

from exercises.ex05.utils import only_evens, sub, concat

#only_evens test
def test_only_odd_numbers() -> None:
    test_list: list[int] = [1, 3, 5, 7]
    assert only_evens(test_list) == []

def test_many_odds_and_evens() -> None:
    test_list: list[int] = [1, 4, 7, 6, 8, 9]
    assert only_evens(test_list) == [4, 6, 8]

def test_with_negative_evens() -> None:
    test_list: list[int] = [-2, 4, 5, -6, -7]
    assert only_evens(test_list) == [-2, 4, -6]

#concat tests
def test_one_list_empty() -> None:
    test_list1: list[int] = []
    test_list2: list[int] = [1, 5, 6]
    assert concat(test_list1, test_list2) == [1, 5, 6]

def test_list_one_element() -> None:
    test_list1: list[int] = [2, -8, 2]
    test_list2: list[int] = [-16]
    assert concat(test_list1, test_list2) == [2, -8, 2, -16]

def test_different_length_lists() -> None:
    test_list1: list[int] = [3, -4, -5]
    test_list2: list[int] = [6, 0, 8, -9, 30, 2]
    assert concat(test_list1, test_list2) == [3, -4, -5, 6, 0, 8, -9, 30, 2]

#sub tests
def test_a_list_empty() -> None:
    test_list: list[int] = []
    test_start: int = 1
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == []

def test_list_many() -> None:
    test_list: list[int] = [1, 2, 3, 4, 5]
    test_start: int = 0
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == [1, 2, 3]

def test_list_with_negatives() -> None:
    test_list: list[int] = [-1, -4, 5, 7]
    test_start: int = 1
    test_end: int = 3
    assert sub(test_list, test_start, test_end) == [-4, 5]
