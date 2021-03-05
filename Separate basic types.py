# https://www.codewars.com/kata/60113ded99cef9000e309be3
def separate_types(seq):
    int1 = [el for el in seq if type(el) == int]
    str1 = [el for el in seq if type(el) == str]
    bool1 = [el for el in seq if type(el) == bool]
    dct = {}
    if int1:
        dct[type(1)] = int1
    if str1:
        dct[type("")] = str1
    if bool1:
        dct[type(1>0)] = bool1
    return dct