https://www.codewars.com/kata/58e230e5e24dde0996000070
def is_prime(n):
    if n <= 1: return False
    for i in range(2, round(n**0.5)+1):
        if n % i == 0: return False
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n