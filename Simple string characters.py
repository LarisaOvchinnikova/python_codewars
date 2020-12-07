# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058
def solve(s):
    res = []
    d, up, low, a = 0, 0, 0, 0
    for el in s:
        if el.isdigit():
            d += 1
        elif el.isalpha():
            if el.isupper():
                up += 1
            else:
                low += 1
        else:
            a += 1
    return [up, low, d, a]