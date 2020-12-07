https://www.codewars.com/kata/5436f26c4e3d6c40e5000282
def sum_of_n(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    arr = []
    step = 1
    el = 0
    for i in range (0, n+1):
        arr.append(el*sign)
        el += step
        step += 1
    return arr