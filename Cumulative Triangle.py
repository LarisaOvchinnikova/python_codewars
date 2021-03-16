# https://www.codewars.com/kata/5301329926d12b90cc000908
def cumulative_triangle(n):
    i  = 0
    step = 1
    last = 0
    while i < n:
        i += 1
        last = last + step
        step += 1
    s = 0
    for i in range(n):
        s += last
        last -= 1
    return s