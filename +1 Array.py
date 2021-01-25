# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
def up_array(arr):
    if arr == []: return None
    for el in arr:
        if el < 0 or el > 9 or type(el)!= int:
            return None
    s = "".join([str(el) for el in arr])
    add = int(s) + 1
    return [int(el) for el in list(str(add))]