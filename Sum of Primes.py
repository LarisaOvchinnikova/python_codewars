# https://www.codewars.com/kata/5902ea9b378a92a990000016/train/python
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, round(n**0.5+1)):
        if n % i == 0:
            return False
    return True
def sum_primes(lower, upper):
    return sum([el for el in range(lower, upper+1) if isPrime(el)])