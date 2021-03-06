# https://www.codewars.com/kata/57aa218e72292d98d500240f
def heron(a,b,c):
    p = (a + b + c) / 2
    return round(((p * (p - a) * (p - b) * (p - c))** 0.5), 2)