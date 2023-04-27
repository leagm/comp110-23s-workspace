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
        new_vals: list[float] = []
        assert step != 0.0
        x: float = start
        for i in range (0, int((stop - start) / step)):
            x = start + step * i
            new_vals.append(x)
        self.values = new_vals

        return None
    
    def sum (self) -> float:
        """Computes the sum of all values in the object values attribute."""
        return_val = float
        return_val = sum(self.values)

        return return_val
    
    def __add__ (self, rhs: Union[float, Simpy]) -> list[float]:
        """This is too long to explain in a docstring. It's Part 5."""
        new_vals: list[float] = []
        if isinstance(rhs, float):
            for i in self.values:
                new_vals.append(i + rhs)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(0, len(self.values)):
                new_vals.append(self.values[i] + rhs.values[i])
        
        return Simpy(new_vals)

    def __pow__ (self, rhs: Union[float, Simpy]) -> list[float]:
        """Similar to Pt 5 but with raising to a power **."""
        new_vals: list[float] = []
        if isinstance(rhs, float):
            for i in self.values:
                new_vals.append(i ** rhs)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(0, len(self.values)):
                new_vals.append(self.values[i] ** rhs.values[i])
        
        return Simpy(new_vals)

    def __eq__ (self, rhs: Union[float, Simpy]) -> list[bool]:
        """When == operand is used will compare the values of two lists and if the values in each list correspond then return True and if else False."""
        new_vals: list[bool] = []
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                if self.values[i] == int(rhs):
                    new_vals.append(True)
                else:
                    new_vals.append(False)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    new_vals.append(True)
                else:
                    new_vals.append(False)

        return new_vals

    def __gt__ (self, rhs: Union[float, Simpy]) -> list[bool]:
        """When > operand is used compares values in two lists and if one value is larger than th eother returns True and if else returns False."""
        new_vals: list[bool] = []
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                if self.values[i] > int(rhs):
                    new_vals.append(True)
                else:
                    new_vals.append(False)
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    new_vals.append(True)
                else:
                    new_vals.append(False)
        
        return new_vals

    def __getitem__ (self, rhs: int) -> float:
        """Reads certain items from the Simpy array."""
        new_vals = self.values[rhs]

        return new_vals

    def __getitem__ (self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Reads certain items but filters them with a mask."""
        new_vals: list[float] = []
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            for i in range(0, len(rhs)):
                if rhs[i] is True:
                    new_vals.append(self.values[i])
        return Simpy(new_vals)