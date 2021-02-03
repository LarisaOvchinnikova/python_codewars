# https://www.codewars.com/kata/528e95af53dcdb40b5000171/
# This function should return n!
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f if n >= 0 else None