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
        if row == column:
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

    for column in table[1]:
        first_n: list[str] = []
        for row in column:
            first_n.append(column[n])
            return_dict += first_n
    return return_dict
