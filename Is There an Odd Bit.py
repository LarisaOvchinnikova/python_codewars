# https://www.codewars.com/kata/5d6f49d85e45290016bf4718/train/python
def any_odd(x):
    b = bin(x)[2:].rjust(32, "0")
    return int([el for i, el in enumerate(b) if i % 2 == 0].count("1") >= 1)
