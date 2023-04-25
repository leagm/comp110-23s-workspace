"""File to define River class."""

__author__ = "730486771"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

<<<<<<< HEAD
=======
from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear
>>>>>>> 11995d82d2a026185397c5323e28767f62a63cd3

class River:
    """Class for the river itself."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int): 
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

<<<<<<< HEAD
    def remove_fish(self, amount: int):
        """Removes fish from the river."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
            
=======
    def check_ages(self):
>>>>>>> 11995d82d2a026185397c5323e28767f62a63cd3
        return None

    def bears_eating(self):
        """Removes fish from river when bear eats and adjusts hunger score."""
        for animal in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                animal.eat(3)
            else:
                fish_to_eat = len(self.fish)
                if fish_to_eat >= 3:
                    self.remove_fish(fish_to_eat)
                    animal.eat(fish_to_eat)
                    self.remove_fish(fish_to_eat)
                else:
                    animal.eat(-(fish_to_eat))

        return None
    
    def check_hunger(self):
        """Checks bear hunger levels to see if bear has enough to live."""
        live_bears = list[Bear]

        for animal in self.bears:
            if animal.hunger_score > 0:
                live_bears.append(animal)
            
        self.bears = live_bears

        return None
<<<<<<< HEAD
                
    def check_ages(self):
        """Checks to see if bear is young enough to live."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

        return None
    
=======
        
>>>>>>> 11995d82d2a026185397c5323e28767f62a63cd3
    def repopulate_fish(self):
        """Repopulates the fish population in the river."""
        new_fish = (len(Fish) // 2) * 4
        self.fish.append(new_fish)

        return None
    
    def repopulate_bears(self):
        """Repopulates the bear population at the river."""
        new_bears = len(Bear) // 2 
        self.bears.append(new_bears)

        return None
    
    def view_river(self):
        """Prints out the current state of the river, the populations of the bears and the fish."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

        return None
            
    def one_river_day(self):
<<<<<<< HEAD
        """Runs the course of a single day in the river."""
=======
        """Simulate one day of life in the river"""
>>>>>>> 11995d82d2a026185397c5323e28767f62a63cd3
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Runs the course of a week in the river."""
        day = 1
        for _ in range(8):
            day += 1
            self.one_river_day()

        return None