"""Functions for EX07."""

__author__ = "730486771"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Given a dict[str, str] invert the keys and values of the given dictionary."""
    new_dict: dict[str, str] = []
    for x in my_dict:
        x = my_dict[x] 
        my_dict[x] = x
        new_dict.append(my_dict)
    return new_dict