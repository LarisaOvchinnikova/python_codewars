https://www.codewars.com/kata/5a946d9fba1bb5135100007c
def is_prime(n):
    if n <= 1: return False
    for i in range(2, round(n**0.5)+1):
        if n % i == 0: return False
    return True

def minimum_number(numbers):
    s = sum(numbers)
    count = 0
    while not is_prime(s):
        s += 1
        count+=1
    return count