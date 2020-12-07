# https://www.codewars.com/kata/5a15a4db06d5b6d33c000018

def sum_nested(lst):
    s=0
    for el in lst:
        if type(el) == int:
            s += el
        elif type(el) == list:
            s += sum_nested(el)
    return s