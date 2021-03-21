# https://www.codewars.com/kata/58b8db810f40ea7788000126
def gcd(a,b):
    while a != b:
        if a > b: a -= b
        else: b -= a
    return a
def fraction(a, b):
    return (a + b)/ gcd(a,b)