# https://www.codewars.com/kata/58fd96a59a9f65c2e900008d
def smallest_integer(matrix):
    arr = []
    for el in matrix:
        arr.extend(el)
    n = 0
    while n in arr:
        n += 1
    return n