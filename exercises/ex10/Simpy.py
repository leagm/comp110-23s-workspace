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
    
    def __fill__ (self, float_val: float, num_vals: int) -> None:
        """Fills a Simpy's values list with a specific number of repeating values."""
        vals_list: list[float] = []
        fill_simpy: str = f"Simpy({vals_list})"

        for _ in range(0, num_vals + 1):
            vals_list.append(float_val)

        return fill_simpy
        
