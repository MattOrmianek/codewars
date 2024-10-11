"""
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"
"""

from collections.abc import Callable
def rot13(message: str) -> str:
    result = ""
    for char in message:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            result += char
    return result

def test_function(f: Callable) -> None:
    assert f("EBG13 rknzcyr.") == "ROT13 example."
    assert f("This is my first ROT13 excercise!") == "Guvf vf zl svefg EBG13 rkprepvfr!"
    print("All tests passed")

if __name__ == "__main__":
    test_function(rot13)
