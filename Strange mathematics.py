# https://www.codewars.com/kata/604517d65b464d000d51381f
def strange_math(n, k):
    s = sorted([str(el) for el in range(1, n+1)])
    return s.index(str(k)) + 1