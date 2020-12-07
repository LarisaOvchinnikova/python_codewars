# Find the middle element
# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python
def gimme(arr):
    middle = sorted(arr)[1]
    return arr.index(middle)