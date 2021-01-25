# https://www.codewars.com/kata/55c02535bf0974404b0000f9
def summation(x):
    return sum(range(1, x+1)) if type(x) == int else "Invalid Value"