#https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/python
def solve(n):
    if n % 10 != 0:
        return -1;
    count = 0;
    while n >= 500:
        n -= 500
        count += 1
    while n >= 200:
        n -= 200
        count += 1
    while n >= 100:
        n -= 100
        count += 1
    while n >= 50:
        n -= 50
        count += 1
    while n >= 20:
        n -= 20
        count += 1
    while n >= 10:
        n -= 10
        count += 1
    return count
# 2 case:
def solve(n):
    s = [500, 200, 100, 50, 20, 10]
    if n % 10 != 0:
        return -1
    count = 0
    for el in s:
        while n >= el:
            n -= el
            count+=1
    return count
#  3 case:
def solve(n):
    if n % 10 != 0: return -1
    value = [500, 200, 100, 50, 20, 10]
    count = 0
    i = 0
    while n > 0:
        count += n // value[i]
        n = n % value[i]
        i+=1
    return count