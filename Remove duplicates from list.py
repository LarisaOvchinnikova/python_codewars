# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118
def distinct(seq):
    s = []
    for el in seq:
        if el not in s:
            s.append(el)
    return s