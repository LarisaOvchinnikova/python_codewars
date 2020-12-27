# https://www.codewars.com/kata/5676f07029da352ba2000065
def is_prime(n):
    if n <= 1: return False
    for i in range(2, round(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def largest(n):
    print(n)
    if type(n) != int or n <= 0: return False
    s = int("9" * n)
    while not is_prime(s):
        s -= 1
    return s