"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""
"""

from collections.abc import Callable


def generate_hashtag(s: str) -> str | bool:
    if s == "":
        return False
    result = "#" + "".join(word.capitalize() for word in s.split())
    return result if len(result) <= 140 else False


def test_function(f: Callable) -> None:
    assert f(" Hello there thanks for trying my Kata") == "#HelloThereThanksForTryingMyKata"
    assert f("    Hello     World   ") == "#HelloWorld"
    assert f("") == False
    print("All tests passed")


if __name__ == "__main__":
    test_function(generate_hashtag)
