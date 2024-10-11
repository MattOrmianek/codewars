"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""

from collections.abc import Callable


def create_phone_number(numbers):
    """
    Create a phone number from a list of 10 integers.
    """
    phone_number_format = "(%d%d%d) %d%d%d-%d%d%d%d"
    return phone_number_format % tuple(numbers)


# This is solution using string formatting:
# return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)


def test_function(f: Callable):
    """
    Test the function with a list of numbers.
    """
    assert f([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert f([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
    assert f([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert f([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
    assert f([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"
    print("All tests passed!")


if __name__ == "__main__":
    test_function(create_phone_number)
