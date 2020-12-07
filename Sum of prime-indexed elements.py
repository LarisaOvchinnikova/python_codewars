#https://www.codewars.com/kata/59f38b033640ce9fc700015b/train/python
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True
def total(arr):
    return sum([el for i, el in enumerate(arr) if isPrime(i)])