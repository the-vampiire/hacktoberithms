from typing import List


def sum_all(list_input: List[int]) -> int:
    """Challenge

        - Write a function called sum_all() that takes a list of two numbers.
        - Return the sum of those two numbers plus the sum of all the numbers between them.

    Notes:
        The lowest number will not always come first

    >>> sum_all([1, 4])
    10
    >>> sum_all([4, 1])
    10
    """
    return sum(range(min(list_input), max(list_input) + 1))
