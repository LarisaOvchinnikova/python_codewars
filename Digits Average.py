# https://www.codewars.com/kata/5a32526ae1ce0ec0f10000b2
import math
def digits_average(n):
    n = [int(el) for el in str(n)]
    while len(n) > 1:
        n = [math.ceil((int(n[i]) + int(n[i+1])) / 2) for i in range(len(n)-1)]
    return n[0]