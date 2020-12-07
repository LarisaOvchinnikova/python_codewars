# https://www.codewars.com/kata/5a7778790136a132a00000c1/train/python
def single_digit(n):
    while n > 9:
        n_bin = (bin(n))[2:]
        n = n_bin.count('1')
    return n

# 2 case
def single_digit(n):
    while n > 9:
        n = bin(n).count('1')
    return n