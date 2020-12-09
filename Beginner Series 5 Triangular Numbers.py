# https://www.codewars.com/kata/56d0a591c6c8b466ca00118b
def is_triangular(t):
    s = 0
    i = 1
    while s < t:
        s += i
        i += 1
    return s == t