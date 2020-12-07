# https://www.codewars.com/kata/5708f682c69b48047b000e07
def multiply(n):
    for i in range(len(str(abs(n)))):
        n *= 5
    return n
