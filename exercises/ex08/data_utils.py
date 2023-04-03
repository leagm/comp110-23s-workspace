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

