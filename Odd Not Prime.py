# https://www.codewars.com/kata/5a9996fa8e503f2b4a002e7a
def is_prime(n):
    if n <= 1: return False
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def odd_not_prime(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 != 0 and not is_prime(i):
            count += 1
    return count