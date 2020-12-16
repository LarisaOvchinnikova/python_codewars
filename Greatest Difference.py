# https://www.codewars.com/kata/56b12e3ad2387de332000041
def diff(arr):
    if arr == []: return False
    res = []
    for el in arr:
        res.append(abs(eval(el)))
    m = max(res)
    i = res.index(m)
    return arr[i] if m > 0 else False