"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730486771"


five_word: str = input("Enter a 5-character word: ")
if (len(five_word) != 5):
    exit(print("Error: Word must contain 5 characters "))
else:
    """Continue"""

single_character: str = input("Enter a single character: ")
if (len(single_character) != 1):
    exit(print("Error: Character must be a single character. "))
else:
    """Continue"""

counter = int = 0

print("Searching for " + single_character + " in " + five_word)
if (five_word[0] == single_character):
    print(single_character + " found at index 0 ")
    counter = counter + 1
else:
    """Continue"""

if (five_word[1] == single_character):
    print(single_character + " found at index 1 ")
    counter = counter + 1
else:
    """Continue"""

if (five_word[2] == single_character):
    print(single_character + " found at index 2 ")
    counter = counter + 1
else:
    """Continue"""

if (five_word[3] == single_character):
    print(single_character + " found at index 3 ")
    counter = counter + 1
else:
    """Continue"""

if (five_word[4] == single_character):
    print(single_character + " found at index 4 ")
    counter = counter + 1
else:
    """Continue"""

if (counter == 1):
    print(counter , " instance of " + single_character + " found in " + five_word)
else:
    """Continue"""

if (counter >= 2):
    print(counter , " instances of " + single_character + " found in " + five_word)
else:
    """Continue"""

if (counter == 0):
    print("No instances of " + single_character + " found in " + five_word)
else:
    """Stop"""
