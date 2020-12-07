# https://www.codewars.com/kata/57f945b77a28db0d750001f2
def count_balls(n):
    s = 0
    x = 1
    for i in range(1,n+1):
        s += x
        x+= i+1
    return s