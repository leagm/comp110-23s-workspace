"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730486771"


class Simpy:
    values: list[float]
    
    # TODO: Your constructor and methods will go here.

    def __init__ (self, my_list: list[float]):
        """Constructor that intializes values attribute of simpy object to the argument passed in."""
        self.values = my_list

        return None
    
    def __str__ (self) -> str:
        """Called whenever simpy object is converted to a str."""
        return_str: str = f"Simpy({self.values})"

        return return_str
    
    def fill (self, float_val: float, num_vals: int):
        """Fills a Simpy's values list with a specific number of repeating values."""
        vals_list: list[float] = []
    
        for _ in range(0, num_vals + 1):
            vals_list.append(float_val)
        self.values = vals_list
        
        return None

    def arange (self, start: float, stop: float, step: float = 1.0):
        """Fills in object values attribute with a range of float values."""
        step != 0.0
        new_vals: list[float] = []
        value: float = start
        while value <= stop:
            if value == start:
                new_vals.append(start)
            else:
                value += step
                new_vals.append(value)
        self.values = new_vals

        return None
    
    def sum (self) -> float:
        """Computes the sum of all values in the object values attribute."""
        return_val = sum(self.values)

        return return_val
    
    def __add__ (self):
        """"""