"""
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']


"""

from collections.abc import Callable


def permutations(s: str) -> list[str]:
    if len(s) == 1:
        return [s]
    result = []
    for i, char in enumerate(s):
        for perm in permutations(s[:i] + s[i + 1 :]):
            result.append(char + perm)
    return list(set(result))


def test_function(f: Callable) -> None:
    assert sorted(f("a")) == ["a"]
    assert sorted(f("ab")) == ["ab", "ba"]
    assert sorted(f("aabb")) == ["aabb", "abab", "abba", "baab", "baba", "bbaa"]
    print("All tests passed")


if __name__ == "__main__":
    test_function(permutations)
