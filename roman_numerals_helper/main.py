"""
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1
Help
+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+
"""
from collections.abc import Callable
symbol_values = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}

class RomanNumerals:
    @staticmethod
    def to_roman(num: int) -> str:
        result = ""
        for symbol, value in symbol_values.items():
            while num >= value:
                result += symbol
                num -= value
        return result

    @staticmethod
    def from_roman(roman_num: str) -> int:
        result = 0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i+2] in symbol_values:
                result += symbol_values[roman_num[i:i+2]]
                i += 2
            else:
                result += symbol_values[roman_num[i]]
                i += 1
        return result


def test_function(f: Callable) -> None:
    assert RomanNumerals.to_roman(1666) == "MDCLXVI"
    assert RomanNumerals.to_roman(1000) == 'M'
    assert RomanNumerals.to_roman(4) == 'IV'
    assert RomanNumerals.to_roman(1) == 'I'
    assert RomanNumerals.to_roman(1990) == 'MCMXC'
    assert RomanNumerals.to_roman(2008) == "MMVIII"

    assert RomanNumerals.from_roman("MDCLXVI") == 1666
    assert RomanNumerals.from_roman("M") == 1000
    assert RomanNumerals.from_roman("IV") == 4
    assert RomanNumerals.from_roman("I") == 1
    assert RomanNumerals.from_roman("MCMXC") == 1990
    assert RomanNumerals.from_roman("MMVIII") == 2008
    print("All tests passed")


if __name__ == "__main__":
    test_function(RomanNumerals)
