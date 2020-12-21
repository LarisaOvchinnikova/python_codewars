# https://www.codewars.com/kata/55b105503da095817e0000b6
def count_vowels(s = ''):
    return len([letter for letter in s if letter.lower() in "aeuio"]) if type(s) == str else None