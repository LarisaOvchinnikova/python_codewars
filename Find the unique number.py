# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
# 6 kyu

def find_uniq(arr):
    lst = sorted(arr)
    return lst[0] if lst[0] != lst[1] else lst[-1]