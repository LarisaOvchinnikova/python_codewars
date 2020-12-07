# https://www.codewars.com/kata/580dda86c40fa6c45f00028a/train/python
def cube_odd(arr):
    s = 0
    for el in arr:
        if type(el) != int:
            return None
        elif el % 2 != 0:
            s += el ** 3
    return s
