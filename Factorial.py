https://www.codewars.com/kata/57a049e253ba33ac5e000212

def factorial(n):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p