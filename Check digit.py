# https://www.codewars.com/kata/5a2e8c0955519e54bf0000bd
def check_digit(number, i1, i2, digit):
    i1, i2 = min(i1, i2), max(i1, i2)
    return str(digit) in str(number)[i1:i2+1]