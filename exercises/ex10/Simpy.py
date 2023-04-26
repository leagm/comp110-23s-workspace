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

    def arange (self, start: float, stop: float, step: float):
        """Fills in object values attribute with a range of float values."""
        range_values: list[float] = []
        n_start: int = int(start)
        n_stop: int = int(stop)
        n_step: int = int(step)
        step != 1.0 or 1
        for _ in range(n_start, n_stop + 1, n_step):
            range_values.append(_)
        for values in range_values:
            float(values)
        self.values = range_values

        return None
    
    def sum (self) -> float:
        """Computes the sum of all values in the object values attribute."""
        return_val = sum(self.values)

        return return_val
    
    def __add__ (self):
        """"""