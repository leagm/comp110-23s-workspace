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
# Lines 28-30 continue the code if an index in the guess does not match the corresponding index in the secret word (in other words, if the index comparison doesn't result in a green box)
            else:
                match_idx = int = 0
                elsewhere = False
# 
                while elsewhere == False and match_idx < len(SECRET_WORD):
                    if (guess[count_idx] == SECRET_WORD[match_idx]):
                        elsewhere = True
                    else:
                        match_idx = match_idx + 1
                if elsewhere == True:
                    emoji = emoji + YELLOW_BOX
                    count_idx = count_idx + 1
                else:
                    emoji = emoji + WHITE_BOX
                    count_idx = count_idx + 1
            emoji = emoji
        print(emoji)
        if (guess == SECRET_WORD):
            print("Woo! You got it! ")
            playing = False
        else:
            print("Not quite, Play again soon! ")
            playing = False
