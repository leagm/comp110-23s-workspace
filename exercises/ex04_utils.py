"""EX04 - Utils"""

__author__ = "730486771"

def all(numbers_list: list, number: int) -> bool:
    """Given a list of integers and an integer, return True if all integers in the list match the integer. Return False if otherwise."""
    list_idx: int = 0
    running: bool = True
    while list_idx < len(numbers_list) - 1 and running is True:
        if number == numbers_list[list_idx]:
            running = True
            list_idx += 1
        else:
            running = False
            return False
    if running is True:
        return True

def max(input: list[int]) -> int:
    """Given a list of integers, return the largest integer in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    int_list_idx: int = 0
    max_number: int = 0

    while int_list_idx < len(input) - 1:
        if input[int_list_idx] > max_number:
            max_number = input[int_list_idx]
            int_list_idx += 1
        else:
            int_list_idx += 1
    return max_number

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given 2 lists of integers returns True if every element at every index is equal in both lists. Returns False if else. Lists do not have to be same length."""
    if len(list_1) != len(list_2):
        return False
    if list_1 == list_2:
        return True
    elif list_1 != list_2:
        return False
