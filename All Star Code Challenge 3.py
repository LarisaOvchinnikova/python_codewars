# https://www.codewars.com/kata/58640340b3a675d9a70000b9
def remove_vowels(s):
    return "".join([el for el in s if el not in "aeuio"])