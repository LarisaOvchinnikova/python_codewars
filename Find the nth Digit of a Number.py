# https://www.codewars.com/kata/577b9960df78c19bca00007e
def find_digit(num, nth):
    num = abs(num)
    if nth <= 0: return -1
    return int(str(num)[::-1][nth-1]) if 0 < nth <= len(str(num)) else 0