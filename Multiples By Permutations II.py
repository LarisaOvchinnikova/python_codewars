# https://www.codewars.com/kata/5ba178be875de960a6000187/train/python
def find_lowest_int(k):
    n = 1
    while True:
        n1 = k * n
        n2 = (k + 1) * n
        s1 = sorted(list(str(n1)))
        s2 = sorted(list(str(n2)))
        if s1 == s2:
            return n
        n += 1