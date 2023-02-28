"""EX04 - Utils"""

__author__ = "730486771"

def all(numbers_list: list, number: int) -> bool:
    """Given a list of integers and an integer, return True if all integers in the list match the integer. Return False if otherwise."""
    list_idx: int = 0
    running: bool = True
    while list_idx < int(len(numbers_list)) - 1 and running is True:
        if number == numbers_list[list_idx]:
            running = True
            list_idx += 1
        else:
            running = False
            return False
    if running is True:
        return True