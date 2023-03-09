"""CQ04 - Zip Function."""

def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Given and list of strings and a list of ints, return a dictionary where the keys are the items from the first list and the values are the items from the second list."""
    output_dictionary: dict[str, int] = {}
    integer_idx: int = 0
    count_idx: int = 0
    if len(list1) != len(list2) or len(list1) == 0 or len(list2) == 0:
        return output_dictionary
    else:
        while integer_idx < (len(list2)) and count_idx < (len(list1)):
            output_dictionary[list1[count_idx]] = list2[integer_idx]
            integer_idx += 1
            count_idx += 1
    return output_dictionary