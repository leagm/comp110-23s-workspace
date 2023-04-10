"""Utils functions for EX08"""

__author__ = "730486771"

from csv import DictReader


# For the read_csv_rows function I created an empty list of dicts to build and return. I pulled data from a file and used DictReader to read the file then I looped through each row of data and appended the values to the return list


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys"""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close
    return result


# For the column_values function I created an empty list of strings to append data to and return. I looped through each row in the input table appending the value in that row at a certain column name to my return list


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list of of all the values in a single column."""
    return_list: list[str] = []

    for row in table:
            return_list.append(row[column])
    return return_list


# For the columnar function I established an empty dictionary to return. Then I looped through keys of one row of table. Next for each key, I made a dictionary entry with all column values and added that those into my return dictionary


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys """
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result


# For the head function I established an empty dict to add my return values to. I then looped through each column in my input table. I then created an empty list to store the values from n number of rows from the table. For each column key I needed to pull a certain number (n) of values from the list, so I made a while loop to do this. I appended these values to the return values list then added these values for each column and row to the return dictionary


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with the first ___(number) rows of data for each column."""
    return_dict: dict[str, list[str]] = {}

    for column in table:
        return_vals: list[str] = []
        i: int = 0
        while i < n and n > 0:
            return_vals.append(table[column][i])
            i += 1
        return_dict[column] = return_vals
    return return_dict
        

# For the select function I established an empty dictionary for my return data. Then I looped through each column in the list of column names that I want to have in my return dict. I added the values at these specific columns from the input table to the output dictionary


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Return table with only certain selected columns of data."""
    return_dict: dict[str, list[str]] = {}

    for column in col_names:
        return_dict[column] = table[column]
    return return_dict
    

# For the concat function I established an empty dictionary to add my combined tables into. Then I looped through each column in the 1st input table and added those values to the return dictionary. Then I looped through the second input table and if the column already existed in the return dict from table1, then I just added the values for that same column from table2. If not, then I added the key-value pair from table2 to the return dictionary


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


# For the count function I created an empty dictionary to add my eventual result to. Then I created a loop that will go through and check if each value in the list is in the new dictionary. If it is, then the value associated with it will increase by 1. If not, it will be added as a key to the dictionary and as it is a newly discovered element, its value will be equal to one since it is the first. The completed dictionary is returned after entire list has been evaluated


def count(my_list: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    return_dict: dict[str, int] = {}
    for value in my_list:
        if value in return_dict:
            return_dict[value] += 1
        else:
            return_dict[value] = 1
    return return_dict