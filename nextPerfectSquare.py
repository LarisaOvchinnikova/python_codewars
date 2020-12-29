# https://www.codewars.com/kata/599f403119afacf9f1000051
def next_perfect_square(n):
    if n < 0: return 0
    n += 1
    while n ** 0.5 % 1 != 0:
        n += 1
    return n