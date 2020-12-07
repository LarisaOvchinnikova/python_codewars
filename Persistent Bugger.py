# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(n):
    count = 0
    n = str(n)
    p = 1
    while len(n) > 1:
        for i in n:
            p = p * int(i)
        n = str(p)
        count += 1
        p = 1
    return count

# 2 case
def persistence(n):
    count = 0
    while n > 9:
        s = 1
        for i in str(n):
            s *= int(i)
        count += 1
        n = s
    return count