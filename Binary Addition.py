# https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python
def add_binary(a,b):
    return bin(a+b)[2:]

# 2 case
def add_binary(a,b):
    s = a + b
    r = ''
    while s > 0:
        r = str(s % 2) + r
        s = s // 2
    return r