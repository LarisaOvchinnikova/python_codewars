# https://www.codewars.com/kata/57073869924f34185100036d
from random import randint
def random_case(x):
    s = ""
    for el in x:
        n = randint(1,10)
        if n < 5:
            s = s + el.upper()
        else:
            s = s + el.lower()
    return s