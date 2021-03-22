# https://www.codewars.com/kata/56bf3287b5106eb10f000899
def move_vowels(s):
    return "".join([el for el in s if not el in "aeuio"] + [el for el in s if el in "aeuio"])
