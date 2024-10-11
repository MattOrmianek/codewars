"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1
"""

from collections.abc import Callable


def next_bigger(n):
    digits = list(str(n))
    length = len(digits)

    for i in range(length - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            # Swap the found digits
            digits[i], digits[j] = digits[j], digits[i]
            break

    digits = digits[: i + 1] + sorted(digits[i + 1 :])

    return int("".join(digits))


def test_function(f: Callable) -> None:
    assert f(12) == 21
    assert f(21) == -1
    assert f(513) == 531
    assert f(2017) == 2071
    assert f(414) == 441
    assert f(144) == 414
    print("All tests passed")


if __name__ == "__main__":
    test_function(next_bigger)
