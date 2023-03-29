"""Functions for EX07."""

__author__ = "730486771"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Given a dict[str, str] invert the keys and values of the given dictionary."""
    inverted_dict: dict[str, str] = {}
    
    for k, v in my_dict:
        if k == k or v == v:
            raise KeyError("Key Error")
    for keys in my_dict:
       value = my_dict[keys]
       inverted_dict[value] = keys
    return inverted_dict