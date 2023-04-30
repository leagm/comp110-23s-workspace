"""Practice Problems for Final Exam."""

def free_biscuits(bball_games: dict[str, list[int]]) -> dict[str, bool]:
    """Check if game points add up to 100+. If yes then map that game as True for free biscuits. If else then map that game as False for free biscuits."""
    return_dict: dict[str, bool] = {}

    for game in bball_games:
        points: int = 0
        for x in bball_games[game]:
            points += x
        if points >= 100:
            return_dict[game] = True
        else:
            return_dict[game] = False
        
    return return_dict


# print(free_biscuits({"UNCvsDuke": [38, 20, 42] , "UNCvsState": [9, 51, 16, 23] }))

def max_key(my_dict: dict[str, list[int]]) -> str:
    """Return key whose list has the highest sum of values."""
    return_str: str = ""

    for x in my_dict:
        highest_value: int = 0
        values: int = 0
        for v in my_dict[x]:
            values += v
            if values > highest_value:
                highest_value = values
                return_str = x
    return return_str


# print(max_key({"a": [1,2,3], "b": [4,5,6]}))

def multiples(my_list: list[int]) -> list[bool]:
    """Return list of bools. Return True if int value in list is a multiple of the previous value. If else return False."""
    return_list: list[bool] = []
    idx: int = 0

    while idx < len(my_list):
        if idx == 0:
            return_list.append(my_list[idx] % my_list[(len(my_list) - 1)] == 0)
        else:
            return_list.append(my_list[idx] % my_list[idx - 1] == 0)
        idx += 1
    return return_list


# print(multiples([2, 3, 4, 8, 16, 2, 4, 2]))

def merge_lists(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Create a dict using values from two lists. List of str are the keys, list of int are the values."""
    return_dict: dict[str, int] = {}

    if len(list1) != len(list2):
        return return_dict
    
    idx: int = 0
    while idx < len(list1):
        return_dict[list1[idx]] = list2[idx]
        idx += 1
    return return_dict


# print(merge_lists(["blue", "yellow", "red"], [5, 2, 4]))

def reverse_multiply(my_list: list[list[int]]) -> list[int]:
    """Double the values in given list, return new list with doubled values in reverse order."""
    return_list: list[int] = []
    i: int = len(my_list) - 1
    while i >= 0:
        return_list.append(my_list[i] * 2)
        i -= 1
    return return_list
 

# print(reverse_multiply([1, 2, 3]))

