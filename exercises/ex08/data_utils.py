"""Utils functions for EX08"""

__author__ = "730486771"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys"""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list of of all the values in a single column."""
    return_list: list[str] = []

    for row in table:
            return_list.append(row[column])
    return return_list


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys """
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with the first ___(number) rows of data for each column."""
    return_dict: dict[str, list[str]] = {}

    for column in table:
        return_vals: list[str] = []
        for item in (table[column]):
            while item in range(1, n + 1):
                return_vals.append(item)
        return_dict[column] = return_vals
    return return_dict
        

def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Return table with only certain selected columns of data."""
    return_dict: dict[str, list[str]] = {}

    for column in col_names:
        return_dict[column] = table[column]
    return return_dict
    

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce new column-based data table made from two combined tables."""
    new_dict: dict[str, list[str]] = {}

    for column in table1:
        new_dict[column] = table1[column]
    for column in table2:
        if column in new_dict:
            new_dict[column] += table2[column]
        else:
            new_dict[column] = table2[column]
    return new_dict


def count(my_list: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    # Created an empty dictionary to add my eventual result to
    return_dict: dict[str, int] = {}
    # Created a loop that will go through and check if each value in the list is in the new dictionary. If it is, then the value associated with it will increase by 1. If not, it will be added as a key to the dictionary and as it is a newly discovered element, its value will be equal to one since it is the first. The completed dictionary is returned after entire list has been evaluated
    for value in my_list:
        if value in return_dict:
            return_dict[value] += 1
        else:
            return_dict[value] = 1
    return return_dict
