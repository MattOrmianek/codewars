"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""

from collections.abc import Callable


def solution(number):
    if number < 0:
        return 0

    multiples = set()
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.add(i)

    return sum(multiples)


def test_function(f: Callable) -> None:
    assert f(6) == 8
    assert f(4) == 3
    assert f(16) == 60
    assert f(3) == 0
    assert f(5) == 3
    assert f(15) == 45
    assert f(0) == 0
    assert f(10) == 23
    print("All tests passed!")


if __name__ == "__main__":
    test_function(solution)
