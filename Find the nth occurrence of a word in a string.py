# https://www.codewars.com/kata/5b1d1812b6989d61bd00004f
def find_nth_occurrence(substring, string, occurrence=1):
    n = 0
    i = 0
    while n < occurrence:
        r = string.find(substring, i)
        i = r + 1
        n += 1
    return r