# https://www.codewars.com/kata/5ec970f05864da001853b55b
import math
def fof(n):
    f = 1
    for i in range(1, n+1):
        f *= math.factorial(i)
    return f