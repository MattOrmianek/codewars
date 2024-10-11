"""
Description:
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

"""

from collections.abc import Callable

def find_it(seq):
    dict_of_apperances = {}
    for number in seq:
        if number in dict_of_apperances:
            dict_of_apperances[number] += 1
        else:
            dict_of_apperances[number] = 1

    for number, apperances in dict_of_apperances.items():
        if apperances % 2 != 0:
            return number

# This is nicer solution:
# for i in seq:
#     if seq.count(i)%2!=0:
#            return i

def test_function(f: Callable) -> None:
    assert f([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
    assert f([1,1,2,-2,5,2,4,4,-1,-2,5]) == -1
    assert f([10]) == 10
    assert f([10, 10, 10]) == 10

if __name__ == "__main__":
    test_function(find_it)
