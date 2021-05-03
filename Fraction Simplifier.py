# https://www.codewars.com/kata/606047f060a707001ae7d5fd
from fractions import gcd
def fraction_simplifier(n, d):
    a = n//gcd(n,d)
    b = d//gcd(n,d)
    return [a, b] if a < b else [n // d, (n % d) //gcd(n % d, d), d // gcd(n % d, d)]
