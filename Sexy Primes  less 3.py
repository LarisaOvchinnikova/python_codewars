# https://www.codewars.com/kata/56b58d11e3a3a7cade000792
def isPrime(n):
    if n<=1: return False
    for i in range(2, round(n**0.5)):
        if n % i == 0: return False
    return True

def sexy_prime(x, y):
    return isPrime(x) and isPrime(y) and abs(x-y) == 6