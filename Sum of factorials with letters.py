# https://www.codewars.com/kata/6000883ce39ca6002648e7f2

import math
def factorial_sum(st):
    s = ''
    for el in st:
        if el.isdigit():
            s += el
        else:
            s += " "
    return sum([math.factorial(int(el)) for el in s.split(" ") if el != ''])