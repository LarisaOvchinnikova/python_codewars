# https://www.codewars.com/kata/59de795c289ef9197f000c48
import re
def remove_bmw(string):
    return re.sub(r'(b|m|w)', "", string, flags=re.I) if type(string) == str else 'This program only works for text.'

# 2 case
def remove_bmw(string):
    if type(string) == str:
        return "".join([el for el in string if el.lower() not in 'bmw'])
    else:
        return 'This program only works for text.'