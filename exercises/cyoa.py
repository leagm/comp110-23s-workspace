"""Ex06 - Choose Your Own Adventure!"""

__author__ = "730486771"

from random import randint

WIZARD: str = "\U0001F9D9"
TROLL: str = "\U0001F9DF"
FAIRY: str = "\U0001F9DA"
ELF: str = "\U0001F9DD"
MERMAID: str = "\U0001F9DC"
SERPENT: str = "\U0001F40D"
KRAKEN: str = "\U0001F419"
DRAGON: str = "\U0001F409"
UNICORN: str = "\U0001F984"

points: int = 40
player: str = ""


def greet() -> None:
    """Greets player with welcome message, provides context of game, asks player for their name."""
    print("Welcome to MYTHICAL RESCUE! ")
    print((f"{WIZARD}: Hello there! I am Grand-dalf the Great! I need your help, mysterious hero! A band of evil trolls have captured some of my mythical creatures and friends. I hope you choose to assist me! "))
    player: str = input("What is your name, hero?: ")
    print(f"{WIZARD}: Well met, {player}! Let us continue on this mythical quest!")


def proceed() -> None:
    """Prompts user to hit the Enter key to continue any text interactions."""
    input("Press Enter to continue...")


def rescue_directions() -> None:
    """Provides more detailed explanation of game rules and directions."""
    print(f"{WIZARD}: Looking for guidance, {player}? Well look no further! Let me explain how you will proceed on this rescue!")
    proceed()
    print(f"{WIZARD}: You will begin your rescue with 40 hero points. There are 7 evil trolls for you to defeat, and 7 creatures to save. There is an evil troll guarding each mythical creature or being.")
    proceed()
    print(f"{WIZARD}: To challenge a troll, you will roll for a random number. If your number is larger than the troll's number, you have defeated the troll and the troll's number will be added to your hero points.")
    proceed()
    print(f"{WIZARD}: If not, then troll's number is subtracted from your hero points and you will roll again against the troll until you either defeat it or run out of hero points.")
    proceed()
    print(f"{WIZARD}: If you and the troll roll the same number, you will roll until they are different. ")
    proceed()
    print(f"{WIZARD}: Each creature or being that you rescue will add a point value to your hero points as you progress.")
    proceed()
    running: bool = True
    while running is True:
        y_or_n_hat = input(f"{WIZARD}: Oh! A question for you, {player}! Do you like my hat? \nY or N?: ")
        if y_or_n_hat == "Y":
            print(f"Many thanks, {player}! I've added 5 points to your hero points!" )
            points = points + 5
        elif y_or_n_hat == "N":
            print(f"I beg you pardon, {player}? Bah! I'm removing 5 hero points for your cheek!")
            points = points - 5
        else:
            print(input("Please enter Y or N: "))
        


def leave_rescue() -> None:
    """Prints farewell message including number of points, exits game."""
    print(f"{WIZARD}: Farewell, hero! I hope we meet again!")
    print(f"Hero Points: {points}")
    exit()


def roll() -> int:
    """Performs random rolls for each stage of the rescue and evaluates the two integers rolled, then returns the points gained or lost."""
    hero_points: int = 0
    running: bool = True

    while running is True:
        roll_1 = randint(1, 20)
        roll_2 = randint(1,20)
        print(f"{WIZARD}: Roll a number!")
        input("Press Enter to continue...")
        print(f"You rolled: {roll_1}")
        print(f"The troll rolled: {roll_2}")
        if roll_1 > roll_2:
            hero_points += roll_2
            running = False
        if roll_1 < roll_2:
            hero_points -= roll_2
            running = True
        if roll_1 == roll_2:
            running = True
    return hero_points


def start_rescue(points: int) -> int:
    """Runs the game, returns final points."""
    hero_points: int = 0
    stage_number: int = 1
    creatures: list[str] = ["placeholder", "fairy", "elf", "mermaid", "sea serpent", "kraken", "dragon", "unicorn"]
    emojis: list[str] = ["PLACEHOLDER", FAIRY, ELF, MERMAID, SERPENT, KRAKEN, DRAGON, UNICORN]
    creatures_points: list[int] = [0, 5, 5, 10, 10, 10, 20, 40]
    running: bool = True

    while running is True and points > 0 and stage_number <= 7:
        print(f"==+== Stage {str(stage_number)}/7 ==+==")
        print(f"Current Hero Points: {points}")
        print(f"{WIZARD}: Let's rescue the {creatures[stage_number]}, {player}!")
        print(f"{TROLL}: *angry* ROOOOAAAARRRR!!!")
        points += roll()
        hero_points += points
        if hero_points > 0:
            print(f"{WIZARD}: Hurrah, {player}! You beat the troll and rescued the {creatures[stage_number]}!")
            print(f"{emojis[stage_number]}: Thank you, {player}! Here are {creatures_points[stage_number]} hero points!")
            points += creatures_points[stage_number]
            stage_number += 1
            running = True
        if hero_points < 0:
            print(f"{WIZARD}: You were unable to rescue the {creatures[stage_number]}. ")
            print(f"{TROLL}: *triumphant* ROOOOAAAARRRR!!!")
            print(f"{emojis[stage_number]} No! Please come back, {player}! ")
            running = False
    if hero_points > 0:
        print(f"{WIZARD}: You've done it, {player}! You have rescued all of the creatures! We are forever grateful!")
    else:
        print(f"{WIZARD}: Dark times are upon us. {player}, you were unable to rescue all of the creatures.")
    return hero_points



def game_loop() -> None:
    """Provides choices after game has ended. Will proceed down a path depending on user input."""
    next_choice: int = input("How would you like to proceed?(Please enter a number choice): \n1. Rescue Directions/Rules \n2. Leave Rescue \n3. Play Again ")
    running: bool = True
    while running is True:
        if next_choice == 1:
            rescue_directions()
        if next_choice == 2:
            leave_rescue()
        if next_choice == 3:
            main()


def next_choice() -> None:
    """Provides main three options for user to choose from, and redirects player on that path based on user input."""
    next_choice: int = input("How would you like to proceed? 1. Rescue Directions/Rules 2. Leave Rescue 3. Start Rescue (Please enter a number choice): ")
    running: bool = True
    while running is True:
        if next_choice == 1:
            rescue_directions
        if next_choice == 2:
            leave_rescue
        if next_choice == 3:
            start_rescue


def main() -> None:
    """Entry point of the game and main game loop."""
    greet()
    next_choice()
    print(f"Rescue over. Final Hero Points: {(start_rescue(points)) == points}")
    game_loop()


if __name__ == "__main__":
    main()
    