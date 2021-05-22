# https://www.codewars.com/kata/583a8bde28019d615a000035
def find_odd_names(lst):
    res = []
    for el in lst:
        s = sum([ord(letter) for letter in el['firstName']])
        if s % 2 != 0:
            res.append(el)
    return res