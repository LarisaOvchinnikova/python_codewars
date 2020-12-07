https://www.codewars.com/kata/57f36495c0bb25ecf50000e7/train/python

def find(n):
    return sum([el for el in range(n+1) if el % 3 == 0 or el % 5 == 0])