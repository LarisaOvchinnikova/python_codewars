# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python
# 5 kyu
def first_non_repeating_letter(string):
    for char in string:
        if (string.lower()).count(char.lower()) == 1:
            return char
    return ""