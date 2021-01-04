# https://www.codewars.com/kata/58475cce273e5560f40000fa
def approx_root(n):
    base = int(n ** 0.5)
    lowest = base ** 2
    greatest = (base + 1) ** 2
    diff_gn = n - lowest
    diff_lg = greatest - lowest
    return round(base + diff_gn / diff_lg, 2)