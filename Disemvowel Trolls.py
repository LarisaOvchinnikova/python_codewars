https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string):
    vowels = "aeuio"
    return "".join([letter for letter in string if not letter.lower() in vowels])