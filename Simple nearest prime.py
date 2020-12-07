#https://www.codewars.com/kata/5a9078e24a6b340b340000b8/train/python
def is_prime(num):
    if num <=1: return False
    for i in range(2, round(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def solve(n):
    x, y = n, n
    while not is_prime(x) and not is_prime(y):
        x -=1
        y +=1
    return x if is_prime(x) else y