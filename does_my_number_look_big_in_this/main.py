"""
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.


"""

from collections.abc import Callable


def narcissistic(value: int) -> bool:
    """
    This function will change value to str, calculate it's digits and checks if every number in value to digits power sums up to value.
    """
    number_str = str(value)
    digits = len(number_str)
    sum_of_powers = 0
    for number in number_str:
        sum_of_powers += int(number) ** digits
    if sum_of_powers == value:
        return True
    return False


# This is nicer solution:
# return value == sum(int(x) ** len(str(value)) for x in str(value))


def test_function(f: Callable) -> None:
    assert f(7) is True, "7 is narcissistic"
    assert f(371) is True, "371 is narcissistic"
    assert f(122) is False, "122 is not narcissistic"
    assert f(4887) is False, "4887 is not narcissistic"
    print("All tests passed!")


if __name__ == "__main__":
    test_function(narcissistic)
