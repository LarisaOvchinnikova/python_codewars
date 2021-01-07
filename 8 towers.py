# https://www.codewars.com/kata/535bea76cdbf50281a00004c
def tower_combination(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f