"""File to define Bear class."""


class Bear:
    """Class for bears in the river"""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes new bear class and class attributes"""

        self.age = 0
        self.hunger_score = 0
        
        return None
    
    def one_day(self):
        """Method that keeps track of bears attributes in one day"""

        self.age += 1
        self.hunger_score -= 1

        return None
    
    def eat(self, num_fish: int):
        """Method that shows what happens when a bear eats"""

        self.hunger_score += num_fish

        return None