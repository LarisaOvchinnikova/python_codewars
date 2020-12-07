#https://www.codewars.com/kata/5572f7c346eb58ae9c000047/train/python
def pattern(n):
    s = ''
    for i in range(1, n+1):
        for j in range(1, i+1):
            s = s + str(i)
        if i < n:
            s = s + "\n"
    return s
# 2 case
def pattern(n):
    return "\n".join([str(x) * x for x in range(1, n + 1)])