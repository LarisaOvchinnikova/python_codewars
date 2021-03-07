# https://www.codewars.com/kata/578dec07deaed9b17d0001b8
def is_prime(n):
    if n <= 1: return False
    for i in range(2, round(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def goldbach_partitions(n):
    a = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n-i):
            a.append(f'{i}+{n - i}')
    return a if n % 2 == 0 else []