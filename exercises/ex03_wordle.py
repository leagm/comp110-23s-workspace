"""EX03 - Structured Wordle."""

__author__ = "730486771"

def contains_char(search_through: str, search_for: str) -> bool:
    """When given two strings, the first of any length, and the second a single character, it will return True if the second string is found anywhere in the first and return False if otherwise"""
    assert len(search_for) == 1
    count_idx: int = 0
    while count_idx < len(search_through):
        if (search_through[count_idx] == search_for):