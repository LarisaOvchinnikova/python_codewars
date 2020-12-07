# https://www.codewars.com/kata/58aed2cafab8faca1d000e20/train/python
def modified_sum(a, n):
    return sum([el**n for el in a]) - sum(a)