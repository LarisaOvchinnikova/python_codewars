# https://www.codewars.com/kata/544d114f84e41094a9000439
def powerof4(n):
    if type(n) != int: return False
    while n > 1:
        n /= 4
    return n == 1