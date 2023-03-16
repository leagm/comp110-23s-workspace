"""EX06 - Create Your Own Adventure!"""

__author__ = "730486771"

WIZARD: str = "\U0001F9D9"


def greet() -> None:
    """Greets player with welcome message, provides context of game, asks player for their name."""
    print("Welcome to MYTHICAL RESCUE! ")
    print((f"{WIZARD}: Hello there! I am Grand-dalf the Great! I need your help, mysterious hero! A band of evil trolls have captured some of my mythical creatures and friends. Can you help me rescue them, hero? "))
    will_you_help = input("Y or N: ")
    playing = True
    while playing:
        if will_you_help == "Y":
            print(f"{WIZARD}: Hurrah! Thank you hero! Let me explain how you will proceed. You will begin your rescue with 40 hero points. There are 7 evil trolls for you to defeat, and 7 creatures to save. There is an evil troll guarding each mythical creature or being. To challenge a troll, you will roll for a random number. If your number is larger than the troll's number, you have defeated the troll and the troll's number will be added to your hero points. If not, then troll's number is subtracted from your hero points and you will roll again against the troll until you either defeat it or run out of hero points. Each creature or being that you rescue will add a point value to your hero points as you progress.")
            player: str = input("What is your name, hero?: ")
            print(f"{WIZARD}: Well met, {player}! Let us continue on this mythical quest!")
            playing = False
        elif will_you_help == "N":
            print((f"{WIZARD}: That's okay, hero. Would you like to leave this rescue? "))
            if leave_rescue(input("Y or N?: ")) == True:
                print(f"{WIZARD}: Farewell, hero! I hope we meet again!")
                playing = False
                quit()
            elif leave_rescue(input("Y or N?: ")) == False:
                print(f"{WIZARD}: Hurrah! Thank you hero! Let me explain how you will proceed. You will begin your rescue with 40 hero points. There are 7 evil trolls for you to defeat, and 7 creatures to save. There is an evil troll guarding each mythical creature or being. To challenge a troll, you will roll for a random number. If your number is larger than the troll's number, you have defeated the troll and the troll's number will be added to your hero points. If not, then troll's number is subtracted from your hero points and you will roll again against the troll until you either defeat it or run out of hero points. Each creature or being that you rescue will add a point value to your hero points as you progress.")
                player: str = input("What is your name, hero?: ")
                print(f"{WIZARD}: Well met, {player}! Let us continue on this mythical quest!")
                playing = False
            else:
                print(input("Please enter Y or N: "))
        else:
            print(input("Please enter Y or N: "))


def leave_rescue(response: str) -> bool:
    """If you responded that you did not want to help the Wizard, you are given the option to leave the game. If you choose to stay,"""
    if response == "Y":
        return True
    if response == "N":
        return False


def main() -> None:
    """Entry point of the game and main game loop."""
    hero_points: int = 40
    stage_number: int = 1
    running: bool = True

    while running is True and hero_points > 0:
        greet()
        next_choice
        print(f"==+== Stage {str(stage_number)}/7 ==+==")
        



if __name__ == "__main__":
    main()
    