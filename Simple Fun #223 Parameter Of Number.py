# https://www.codewars.com/kata/5902f1839b8e720287000028
def parameter(n):
    arr = [int(el) for el in str(n)]
    n1 = sum(arr)
    n2 = 1
    for el in arr:
        n2 *= el
    a, b = n1, n2
    while n1 != n2:
        if n1 > n2: n1 -= n2
        else: n2 -= n1
    return a * b / n1