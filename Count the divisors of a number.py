# https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python
def divisors(n):
    return len([el for el in range(1, n+1) if n % el == 0])