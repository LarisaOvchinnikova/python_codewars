# https://www.codewars.com/kata/559e10e2e162b69f750000b4/train/python
def dominator(arr):
    lst = [el for el in arr if arr.count(el)>len(arr)/2]
    return lst[0] if len(lst) > 0 else -1