https://www.codewars.com/kata/5ce04eadd103f4001edd8986
import math
def solution(n,b):
    res = []
    if b == 0: return []
    i = -int(math.log2(b))-1
    bin_b = bin(b)[2:].rjust(n,"0")
    for num in range(2**n):
        bin_n = bin(num)[2:].rjust(n,"0")
        if abs(i) <= n and bin_n[i] == bin_b[i] :
            res.append(num)
    return res