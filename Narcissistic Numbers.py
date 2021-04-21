# https://www.codewars.com/kata/56b22765e1007b79f2000079
def is_narcissistic(num):
    return sum([int(el)**len(str(num)) for el in str(num)]) == num