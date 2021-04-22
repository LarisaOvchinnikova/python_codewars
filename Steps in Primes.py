# https://www.codewars.com/kata/5613d06cee1e7da6d5000055
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, round(n**0.5+1)):
        if n % i == 0:
            return False
    return True

def step(g, m, n):
    for i in range(m, n - g + 1):
        if is_prime(i) and is_prime(i+g):
            return [i,i+g]