# https://www.codewars.com/kata/582aafca2d44a4a4560000e7
def keep_order(arr, val):
    arr.append(val)
    arr = sorted(arr)
    return arr.index(val)