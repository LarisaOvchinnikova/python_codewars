# https://www.codewars.com/kata/5a2b7edcb6486a856e00005b
def check_vowel(string, position):
    return string[position].lower() in "aeuio" if 0 <= position < len(string) else False