# https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/train/python
def reverse(n):
    r = 0
    while n > 0:
        last = n % 10
        r = r * 10 + last
        n = n//10
    return r

def reverse(n):
    return int(str(n)[::-1])