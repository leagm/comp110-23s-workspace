"""EX03 - Structured Wordle."""

__author__ = "730486771"

# Lines 6-7 define the function contains_char function to search for a single character string in a string of any length 
def contains_char(search_through: str, search_for: str) -> bool:
    """When given two strings, the first of any length, and the second a single character, return True if the second string is found anywhere in the first and return False if otherwise"""
# asserted length of seacrh_for to be 1 so that the function is only searching for one character in the string being searched through 
    assert len(search_for) == 1
# count_idx to keep track of which index the function body is examining
    count_idx: int = 0
# elsewhere defined to keep function body running and serve as the return boolean value
    elsewhere = False
# Lines 15-20 evaluate whether the single character search_for is found at any of the indices in the guessed string search_through using count_idx which will increase by 1 until it reaches the length of search_through, or until it finds an index where elsewhere is True. If it is found, the while loop ends and the value of elsewhere (True) is retured. If search_for is not found anywhere in search_through, the loop ends and elsewhere (False) is returned
    while elsewhere == False and count_idx < len(search_through):
        if (search_through[count_idx] == search_for):
            elsewhere = True
        else:
            count_idx = count_idx + 1
    return elsewhere

# Lines 23-24 define the function emojified to, given two strings of equal length, one which is a secret and the other a guess, return a string of emojis that will codify according to the placement/existence of characters within guess words
def emojified(guess_word: str, secret_word: str) -> str:
    """Given two strings of equal length, one which is a guess and the other which is a secret, return a string of emojis that will codify according to the placement/existence of characters within guess words"""
# Assert the length of the guess word to the length of the secret word so that the user can only enter a guess that is the same length as the secret word
    assert len(guess_word) == len(secret_word)
# Lines 28-30 assign the unicode for the colored box emojis used in this function
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
# counter_idx defined to keep track of which index in the secret word and guess word are being examined
    counter_idx: int = 0
# Initially empty string called emoji created to keep track of the returned emojis when each guess is evaluated
    emoji: str = ""
# Lines 36-39 start a while loop which check whether any green boxes should be placed at any of the indices in the emoji string, i.e. if a character at an index in the secret word is exactly equal to the a character at the same index in the guess word
    while counter_idx < len(secret_word):
        if (guess_word[counter_idx] == secret_word[counter_idx]):
            emoji = emoji + GREEN_BOX
            counter_idx = counter_idx + 1
# Lines 41-47 checks whether any yellow or white boxes should be added to the emoji string after all indices have been checked for green boxes. First it checks for yellow using the contains_char function to check each character in the guess word with all indices of the secret word. If a single character from the guess word is found at any index of the secret word, a yellow box is added to the emoji string at that index. If there are no instances of a character from the guess word anywhere in the secret word, a white box will be added to the emoji string
        else:
            if contains_char(secret_word, guess_word[counter_idx]) == True:
                emoji = emoji + YELLOW_BOX
                counter_idx = counter_idx + 1
            else:
                emoji = emoji + WHITE_BOX
                counter_idx = counter_idx + 1
# Function returns the completed emoji string after all indices have been assigned a colored box
    return emoji

# Lines 52-53 define the function input_guess which will take the length of the secret guess and prompt the user for a guess of that length. If incorrect length guess is inputted, it will continually prompt the user for the correct length guess until the user enters a correct length guess. Once a correct length guess is entered, the function will return that guess
def input_guess(correct_length: int) -> str:
    """Given integer length of a guess, prompt the user for a guess of the correct length. When correct length guess is entered by user, function returns that guess"""
# Line 55 asks for an input or a guess from the user that is the correct length, or in the context of this code the length of the secret word
    guess = input(f"Enter a {str(correct_length)} character word: ")
# boolean playing to keep body of function running. If boolean playing is True, the code keeps running. If false, the while loop ends
    playing = True
# Lines 59-64 checks if the length of the user's input guess is the correct length. If the lenth of the guess is not equal to the correct length, then the user is prompted to enter a guess of the correct length, and the while loop runs again. Once the correct length guess is inputted, the boolean is False and the while loop ends
    while playing:
        if (len(guess) != correct_length):
            guess: str = input(f"That was not {str(correct_length)} letters! Try again: ")
            playing = True
        if (len(guess) == correct_length):
            playing = False
# Once the correct length guess has been inputted, the function returns this correct length guess
    return guess

# Lines 69-70 define the main function which serves as the entrypoint to the entire game loop and facilitates the order and actions of the whole game code
def main() -> None:
    """The entrypoint of the program and main game loop."""
# The secret word which the user will be trying to guess during the game is defined 
    SECRET: str = "codes"
# Integer assigned to count the turn number that the user is on in the game
    turn_number: int = 1
# Boolean running keeps the game running. When True, the game continues. When False, the game is over
    running = True
# Line 78 begins a while loop which runs as long as the game is running and the turn number is less than or equal to 6
    while running == True and turn_number <= 6:
# The number of turns out of six is printed at the top of each turn
        print(f"=== Turn {str(turn_number)}/6 ===")
# The function input_guess is called here to return a guess input from the user of the length of the secret word. The returned guess becomes the guess_word
        guess_word = input_guess(len(SECRET))
# The function emojified is called to print the resulting emoji string given how the guess word compares to the secret word
        print (emojified(guess_word, SECRET))
# Lines 86-89 end the game if the secret word is guessed by the user. It prints a message telling the user how many turns out of six it took for the correct guess to be entered then playing False and the game is over
        if (guess_word == SECRET):
            print (f"You won in {str(turn_number)}/6 turns! ")
            print()
            running = False
# Lines 91-93 continue the code if the user has not guessed the secret word yet. It will add 1 to the turn counter, running is True, so the code loops back to the top for another turn
        else:
            turn_number = turn_number + 1
            running = True
# Lines 95-97 end the game if the user has not guessed the secret word on the sixth turn. The while loop on Line 78 will prevent the user from exceeding six turns. This if statement prints a message telling the user to try again tomorrow and the code ends
    if (turn_number > 6):
        print ("X/6 - Sorry, try again tomorrow! ")
        print()

# Lines 100-101 make it possible for the program to be run as a module and makes it possible for other modules to import the functions in this program
if __name__ == "__main__":
    main()