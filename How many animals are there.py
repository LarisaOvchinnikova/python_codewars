# https://www.codewars.com/kata/593406b8f3d071d83c00005d
def count_animals(s):
    lst = s.split()
    sum = 0
    for el in lst:
        if el.isdigit():
            sum = sum + int(el)
    return sum