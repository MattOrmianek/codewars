"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""

from collections.abc import Callable


def row_sum_odd_numbers(n: int) -> int:
    return n**3


def test_function(f: Callable) -> None:
    assert f(1) == 1
    assert f(2) == 8
    assert f(13) == 2197
    assert f(19) == 6859
    assert f(41) == 68921
    print("All tests passed!")


if __name__ == "__main__":
    test_function(row_sum_odd_numbers)
