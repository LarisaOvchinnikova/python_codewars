# https://www.codewars.com/kata/5c8e99ba171e834117a0e905
def binary_sort(s):
    return "".join(sorted([el for el in s if el in "01"]))