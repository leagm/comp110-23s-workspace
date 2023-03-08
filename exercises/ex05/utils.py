"""Functions and Implementations for EX05."""

__author__ = "730486771"


def only_evens(list_ints: list[int]) -> list:
    """Given a list of integers, return a list of only the even integers from given list."""
    even_nums: list[int] = list()
    for number in list_ints:
        if number % 2 == 0:
            even_nums.append(number)
    return even_nums


def concat(list1: list[int], list2: list[int]) -> list:
    """Given two lists of integers, return a list which contains all elements of first list then all elements of second list."""
    concat_list: list[int] = []
    for integer in list1:
        concat_list.append(integer)
    for ints in list2:
        concat_list.append(ints)
    return concat_list


def sub(a_list: list[int], start: int, end: int) -> list:
    """Given a list of integers, and two integers, the first of which is a start index and the second and end index-1, return a list which is a subset of the given list between the two given indexes."""
    sub_list = []
    if (start < 0):
        start = 0
    if (end > (len(a_list) - 1)):
        end = len(a_list)
    if (0 == len(a_list)) or (start >= len(a_list)) or (end <= 0) or (start >= end):
        return sub_list
    else: 
        for num in range(start, end):
            sub_list.append(a_list[num])
        return sub_list