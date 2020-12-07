# https://www.codewars.com/kata/55cb0597e12e896ab6000099/train/python
def arithmetic_sequence_sum(a, r, n):
    s = 0
    for i in range(1, n+1):
        s = s + a
        a = a + r
    return s