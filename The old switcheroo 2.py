https://www.codewars.com/kata/55d6a0e4ededb894be000005
def encode(string):
    alph = ' abcdefghijklmnopqrstuvwxyz'
    return "".join([str(alph.index(el.lower())) if el.isalpha() else el for el in string])
