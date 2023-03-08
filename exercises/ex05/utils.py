"""Functions and Implementations for EX05"""

__author__ = "730486771"

def only_evens(list_ints: list[int]) -> list:
    """Given a list of integers, return a list of only the even integers from given list"""
    even_nums: list[int] = list()
    for number in list_ints:
        if number % 2 == 0:
            even_nums.append(number)
    return even_nums

def concat(list1: list[int], list2: list[int]) -> list:
    """Given two lists of integers, return a list which contains all elements of first list then all elements of second list"""
    for integer in list2:
        list1.append(integer)
    return list1

def sub(a_list: list[int], start: int, end: int) -> list:
    """Given a list of integers, and two integers, the first of which is a start index and the second and end index-1, return a list which is a subset of the given list between the two given indexes"""
    a_list: list[int] = input(list())
    sub_list: list = list()
    for num in range(start, end):
        sub_list.append(num)
    return sub_list