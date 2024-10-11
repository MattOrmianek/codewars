"""
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:

"""

from collections.abc import Callable


def perimeter(n):

    def fibonacci(n):
        fib_sequence = [0, 1]
        for _ in range(2, n + 3):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n + 2]

    return 4 * (fibonacci(n + 1) - 1)


def test_function(f: Callable) -> None:
    assert f(5) == 80
    assert f(7) == 216
    assert f(20) == 114624
    assert f(30) == 14098308
    assert f(100) == 6002082144827584333104
    assert (
        f(500)
        == 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504
    )
    print("All tests passed")


if __name__ == "__main__":
    test_function(perimeter)
