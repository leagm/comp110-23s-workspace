"""Functions for EX07."""

__author__ = "730486771"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values."""
    # Created an empty dictionary to put inverted values into
    inverted_dict: dict[str, str] = {}
    # Raises an error is duplicate values are found in the input dictionary
    if len(set(dict.values(my_dict))) != len(dict.values(my_dict)):
        raise KeyError("Error: value duplicates")
    # Looks through dictionary values and reassigns those values as the keys in the new inverted dictionary
    for keys in my_dict:
        value = my_dict[keys]
        inverted_dict[value] = keys
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Given a dict[str, str] it should return a str which is the color that appears most frequently in the dictionary."""
    if color_dict == {}:
        message: str = "Enter a dictionary with values!"
        return message
    # Created a list of just the values of the input dictionary because I'm focusing on the colors
    color_list: list[str] = list(dict.values(color_dict))
    # Created a counter that keeps track of which value occurs in the list the most.
    current_most_frequent = 0
    # Created a str that will be defined as the favorite color and returned.
    current_fav_color = str
    # Created a loop that looks through each element of the list and counts how many times that element is found. As the loop moves through the list, whichever element/color has the higest frequency is updated to be the current most frequent value. Finally, the most frequent value is assigned to the favorite color variable and returned
    for x in color_list:
        if color_list.count(x) > current_most_frequent:
            current_most_frequent = color_list.count(x)
            current_fav_color = x
    return current_fav_color


def count(my_list: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    if my_list == []:
        message: str = "Enter a list with values!"
        return message
    # Created an empty dictionary to add my eventual result to
    return_dict: dict[str, int] = {}
    # Created a loop that will go through and check if each value in the list is in the new dictionary. If it is, then the value associated with it will increase by 1. If not, it will be added as a key to the dictionary and as it is a newly discovered element, its value will be equal to one since it is the first. The completed dictionary is returned after entire list has been evaluated
    for value in my_list:
        if value in return_dict:
            return_dict[value] += 1
        else:
            return_dict[value] = 1
    return return_dict
