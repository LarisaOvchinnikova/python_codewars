# https://www.codewars.com/kata/56cf0eb69e14db4897000b97
def is_prime(n):
    if n <= 1: return False
    for i in range(2, round(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    a = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n-i):
            a.append( [i, n - i])
    return a