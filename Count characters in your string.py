# https://www.codewars.com/kata/52efefcbcdf57161d4000091/solutions/python
def count(s):
    dct = {}
    if s == '':
        return {}
    return {letter: s.count(letter) for letter in s}