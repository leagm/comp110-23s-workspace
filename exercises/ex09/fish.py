"""File to define Fish class."""


class Fish:
    """Class for fish in the river."""

    age: int

    def __init__(self):
        """Method to new fish class and initialize fish attributes."""
        self.age = 0

        return None
    
    def one_day(self):
        """Method to keep track of fish attributes in one day."""
        self.age += 1

        return None