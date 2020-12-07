# https://www.codewars.com/kata/58f475735e78fde4a2000011/train/python
def sum1(array):
    return sum([el*(i+1) for i, el in enumerate(array)])