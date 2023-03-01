"""EX04 - Utils"""

__author__ = "730486771"

# Lines 6-7 define the function all. It's parameters are a list of integers called numbers_list, and an integer called number. It returns True if all of the integers in the list are equal to the integer. It returns False if otherwise
def all(numbers_list: list, number: int) -> bool:
    """Given a list of integers and an integer, return True if all integers in the list match the integer. Return False if otherwise."""
# Lines 9 defines list_idx to keep track of what index is being evaluated in the list. Line 10 defines a boolean called running which will keep the body of this function going
    list_idx: int = 0
    running: bool = True
# Line 12 starts a while loop that will run while the boolean running is True and while the list_idx counter remains less than the amount of indexes in the list
    while list_idx < len(numbers_list) - 1 and running is True:
# Lines 14-16 checks if the first index of the list is equal to the integer. If it is, then it will check the next index and so on until the end of the list
        if number == numbers_list[list_idx]:
            running = True
            list_idx += 1
# Lines 18-20: If at any point while checking through the indexes the integer does not equal an integer in the list, then the loop stops running and the function returns False becuase the list is not composed of only the same integer
        else:
            running = False
            return False
# Lines 22-23 is stepped into only if the boolean running remains True, which means that every index of the list has been equal to the integer. This means True is returned
    if running is True:
        return True

# Lines 26-27 define a function called max. Its parameter is a list of integers called input. It will return the largest integer in the list.
def max(input: list[int]) -> int:
    """Given a list of integers, return the largest integer in the list."""
# Lines 29-30 will raise an error if the function is given an empty list
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
# Line 33 defines a counting index xalled int_list_idx which keeps track of the index being evaluated in the list. Line 34 defines the max number as being zero
    int_list_idx: int = 0
    max_number: int = 0

# Line 37 starts a while loop which will run while the index being evaluated is less than the number of indexes in the list
    while int_list_idx < len(input) - 1:
# Lines 39-41 check if the first index of the list is greater than 0, and if it is, then the integer at the first index becomes the max number and the code re-enters thsi if statement. It will wontinue to compare the reassigned max number to the next index in the list until the entire list has been evaluated and the true max number is found
        if input[int_list_idx] > max_number:
            max_number = input[int_list_idx]
            int_list_idx += 1
# Lines 43-44 will also increase the index counter to continue through evaluation even if the index evaluated was not greater than the max number. The max number is not redefined and the code loops back to the beginning to evaluate the max number against the next index
        else:
            int_list_idx += 1
# Line 46 returns the max number after the entire list has been evaluated 
    return max_number

# Lines 49-50 define a function called is_equal. Its parameters are 2 lists of integers. It returns the boolean True if the lists are exactly equal, i.e. if every value at each index is the same. It returns False if otherwise
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given 2 lists of integers returns True if every element at every index is equal in both lists. Returns False if else. Lists do not have to be same length."""
# Lines 52-53 evaluate if the length of the two lists is the same. If they are not the same length then the function ends and returns False because if they are not the same length it is impossible for them to be exactly equal
    if len(list_1) != len(list_2):
        return False
# Lines 55-56 check if the lists are exactly equivalent to eachother. If they are, the function ends and returns True
    if list_1 == list_2:
        return True
# Lines 58-59 will check again if the lists are not equal to eachother, and if they are not exactly equal the function ends and returns False
    elif list_1 != list_2:
        return False
