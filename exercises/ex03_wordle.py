"""EX03 - Structured Wordle."""

__author__ = "730486771"

def contains_char(search_through: str, search_for: str) -> bool:
    """When given two strings, the first of any length, and the second a single character, return True if the second string is found anywhere in the first and return False if otherwise"""
    assert len(search_for) == 1
    count_idx: int = 0
    while count_idx < len(search_through):
        if (search_through[count_idx] == search_for):
            return True
        else:
            count_idx = count_idx + 1
            if (search_through != search_for):
                return False

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
            elsewhere = False
            while elsewhere is False:
                if (contains_char(secret_word, guess_word[counter_idx]) == True):
                    emoji = emoji + YELLOW_BOX
                    counter_idx = counter_idx + 1
                else:
                    emoji = emoji + WHITE_BOX
                    counter_idx = counter_idx + 1
        emoji = emoji
    print(emoji)
