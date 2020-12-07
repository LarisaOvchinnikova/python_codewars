https://www.codewars.com/kata/54ff3102c1bad923760001f3
def getCount(inputStr):
    num_vowels = 0
    vowels = "aeiou"
    for letter in inputStr:
        if letter in vowels:
            num_vowels += 1

    return num_vowels

# ---- 2 case
def getCount(inputStr):
    num_vowels = [1 for letter in inputStr if letter in "aeuio"].count(1)
    return num_vowels

# -----3 case
def getCount(inputStr):
    num_vowels = [1 for letter in inputStr if letter in "aeuio"]
    return len(num_vowels)