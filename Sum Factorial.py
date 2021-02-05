# https://www.codewars.com/kata/56b0f6243196b9d42d000034
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def sum_factorial(lst):
    return sum([fact(el) for el in lst])