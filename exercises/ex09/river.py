"""File to define River class"""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def remove_fish(self, amount: int):
        for animal in range(0, amount):
            self.fish.pop(animal)

        return None

    def bears_eating(self):

        for animal in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
            animal.eat(3)

        return None
    
    def check_hunger(self):

        live_bears = list[Bear]

        for animal in self.bears:
            if animal.hunger_score < 0:
                live_bears.pop(animal)
            if animal.hunger_score >= 0:
                live_bears.append(animal)
        self.bears = live_bears

        return None
                
    def check_ages(self):

        live_fish = list[Fish]
        live_bears = list[Bear]

        for animal in self.fish:
            if animal.age <= 3:
                live_fish.append(animal)
        self.fish = live_fish
        for animal in self.bears:
            if animal.age <= 5:
                live_bears.append(animal)
        self.bears = live_bears
        
        return None
        
    def repopulate_fish(self):

        new_fish = (len(self.fish) // 2) * 4
        self.fish.append(new_fish)

        return None
    
    def repopulate_bears(self):

        new_bears = len(self.bears) // 2 
        self.bears.append(new_bears)

        return None
    
    def view_river(self):

        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

        return None
            
    def one_river_day(self):
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

        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        
        return None