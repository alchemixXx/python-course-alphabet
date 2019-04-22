from typing import List, Dict, Union, Generator
import random
import string

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """

    return [member.update({member.keys(): member.values().capitalize()}) for member in data if
            type(member.values()) == str]


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for member in data:
        for key in redundant_keys:
            member.pop(key)
    return data
    # return [{key: value for key, value in member.items() if key not in redundant_keys} for member in data]


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    return [({key: value for key, value in member.items()}) for member in data if value in member.values()]


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """

    return min(data, default=None)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """

    min_len = string.ascii_letters * 1000
    for item in data:
        if len(str(item)) < len(min_len):
            min_len = str(item)
    return min_len if len(data) > 0 else None


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    # return [member for member in data if (min([member.get('age', None) for member in data if 'age' in member.keys()])) in member.values()][0]
    return [member for member in data if (min(map(lambda x: x.get('age', 10000), data))) in member.values()][0]


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """

    return max([item for sublist in data for item in sublist])


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data)


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    return sum([ord(item) for item in text])


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    # for number in range(2, 201):
    #     checker = 0
    #     for test_number in range(2, number):
    #         if number % test_number == 0:
    #             checker = 1
    #             continue
    #     if checker == 0:
    #         yield number

    return (number for number in range(2, 201) if all([1 if number % x != 0 else 0 for x in range(2, number)]))


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """
    return [random.choice(string.ascii_lowercase) for _ in range(20)]
