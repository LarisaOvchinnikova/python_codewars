# https://www.codewars.com/kata/55d410c492e6ed767000004f
def vowel_2_index(string):
    return ''.join([str(i+1) if el.lower() in "aeuio" else el for i, el in enumerate(string)])