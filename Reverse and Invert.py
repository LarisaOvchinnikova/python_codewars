# https://www.codewars.com/kata/5899e054aa1498da6b0000cc
def reverse_invert(lst):
    return [-int(str(el)[::-1]) if el >= 0 else int(str(abs(el))[::-1]) for el in lst if type(el) == int]