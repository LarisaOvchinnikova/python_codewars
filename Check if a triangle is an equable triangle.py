# https://www.codewars.com/kata/57d0089e05c186ccb600035e
def equable_triangle(a,b,c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s ==  p * 2