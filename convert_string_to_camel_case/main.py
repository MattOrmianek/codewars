"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

import re
from collections.abc import Callable


def to_camel_case(text):
    return re.sub(r"[-_](\w)", lambda m: m.group(1).upper(), text)


def test_function(f: Callable) -> None:
    assert f("the-stealth-warrior") == "theStealthWarrior"
    assert f("The_Stealth_Warrior") == "TheStealthWarrior"
    assert f("The_Stealth-Warrior") == "TheStealthWarrior"
    print("All tests passed")


if __name__ == "__main__":
    test_function(to_camel_case)
