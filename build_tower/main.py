"""
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
"""

from collections.abc import Callable


def tower_builder(n_floors: int) -> list[str]:
    stars = [2 * i + 1 for i in range(n_floors)]
    spaces = [n_floors - i - 1 for i in range(n_floors)]
    return [f"{space * ' '}{star * '*'}{space * ' '}" for space, star in zip(spaces, stars)]


def test_function(f: Callable) -> None:
    assert f(1) == [
        "*",
    ]
    assert f(2) == [" * ", "***"]
    assert f(3) == ["  *  ", " *** ", "*****"]
    print("All tests passed")


if __name__ == "__main__":
    test_function(tower_builder)
