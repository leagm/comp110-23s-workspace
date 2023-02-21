"""EX03 - Structured Wordle."""

__author__ = "730486771"

def contains_char(search_through: str, search_for: str) -> bool:
    """When given two strings, the first of any length, and the second a single character, return True if the second string is found anywhere in the first and return False if otherwise"""
    assert len(search_for) == 1
    count_idx: int = 0
    elsewhere = False
    while elsewhere == False and count_idx < len(search_through):
        if (search_through[count_idx] == search_for):
            elsewhere = True
        else:
            count_idx = count_idx + 1
    return elsewhere

def emojified(guess_word: str, secret_word: str) -> str:
    """Given two strings of equal length, one which is a guess and the other which is a secret, return a string of emojis that will codify according to the placement/existence of characters within guess words"""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    counter_idx: int = 0
    emoji: str = ""
    while counter_idx < len(secret_word):
        if (guess_word[counter_idx] == secret_word[counter_idx]):
            emoji = emoji + GREEN_BOX
            counter_idx = counter_idx + 1
        else:
            if contains_char(secret_word, guess_word[counter_idx]) == True:
                emoji = emoji + YELLOW_BOX
                counter_idx = counter_idx + 1
            else:
                emoji = emoji + WHITE_BOX
                counter_idx = counter_idx + 1
    return emoji

def input_guess(correct_length: int) -> str:
    """Given integer length of a guess, prompt the user for a guess of the correct length. When correct length guess is entered by user, function returns that guess"""
    guess = input(f"Enter a {str(correct_length)} character word: ")
    playing = True
    while playing:
        if (len(guess) != correct_length):
            guess: str = input(f"That was not {str(correct_length)} letters! Try again: ")
            playing = True
        if (len(guess) == correct_length):
            playing = False
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    turn_number: int = 1
    running = True
    while running == True and turn_number < 6:
        print(f"=== Turn {str(turn_number)}/6 ===")
        guess_word = input_guess(5)
        print (emojified(guess_word, SECRET))
        if (guess_word == SECRET):
            print (f"You won in {str(turn_number)}/6 turns! ")
            running = False
        else:
            turn_number = turn_number + 1
            running = True
    if (turn_number == 6 and guess_word != SECRET):
        print ("X/6 - Sorry, try again tomorrow! ")
        running = False