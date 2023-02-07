"""EX02 - One Shot Wordle. """

__author__ = "730486771"

SECRET_WORD: str = "python"
guess: str = input(f"What is your {len(SECRET_WORD)}-letter guess? ")
# playing boolean to heep entire while loop code running until made True
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# count_idx to keep track of which index the code is examining or comparing
count_idx: int = 0
emoji: str = ""

# Lines 17-20 start the code and evaluate the length of the guess to ensure that it is the same length of the secret word
while playing:
    if (len(guess) != len(SECRET_WORD)):
        guess: str = input(f"That was not {len(SECRET_WORD)} letters! Try again: ")
        playing = True
# Lines 22-26 begin a second while loop and the first if statement which evaluates if/where a green box may be placed        
    else:
        while count_idx < len(SECRET_WORD):
            if (guess[count_idx] == SECRET_WORD[count_idx]):
                emoji = emoji + GREEN_BOX
                count_idx =  count_idx + 1
# Lines 28-30 continue the code if the indices do not evaluate to a green box. Match_idx is reset to 0 so that the following while loop will compare the guess index to all indices of the secret word. The bool elsewhere is set to False to keep the following while loop running
            else:
                match_idx = int = 0
                elsewhere = False
# Lines 32-34 start an embedded while loop which will compare each index of the guess word to every index of the secret word as long as the bool elsewhere remains False
                while elsewhere == False and match_idx < len(SECRET_WORD):
                    if (guess[count_idx] == SECRET_WORD[match_idx]):
                        elsewhere = True
# Lines 36-37 tell the program to increase the index counter for the secret word (match_idx) if the indices of the secret word do not match with that of the guess word.
                    else:
                        match_idx = match_idx + 1
# Lines 39-41 provide a further direction for once the if and else statements above have been evaluated. If elsewhere was assigned to be True above, then a yellow box emoji should be added to the emoji string at the appropriate index, count_idx should be increased and then the while loop should start over with a new index in the guess to be compared to all indices of the secret word
                if elsewhere == True:
                    emoji = emoji + YELLOW_BOX
                    count_idx = count_idx + 1
# Lines 43-45 tell the program that if there were no matches for an index in the guess word with any of the indices in the secret word then a white box emoji should be added to the appropriate index in the emoji string
                else:
                    emoji = emoji + WHITE_BOX
                    count_idx = count_idx + 1
# Lines 47-48 finalize the placement of the emoji boxes within the emoji string before printing the string result
            emoji = emoji
        print(emoji)
# Lines 50-52 print the message "Woo! You got it! " if the user correctly guessed the secret word. The bool playing will be assigned False in this instance because the game has been won and playing is no longer True
        if (guess == SECRET_WORD):
            print("Woo! You got it! ")
            playing = False
# Lines 54-56 print the message "Not quite. Play again soon!  " if the user's inputted guess was not exactly equal to the secret word. The bool playing is assigned false in this instance because the one guess has been fully evaluated and was not correct so the game is over and playing is no longer True
        else:
            print("Not quite. Play again soon! ")
            playing = False
# Finished the code! :)