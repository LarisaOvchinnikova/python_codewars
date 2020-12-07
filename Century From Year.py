# Century From Year
# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097

def century(year):
    import math
    return math.ceil(year/100)

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
