# https://www.codewars.com/kata/59781c959b82f6ee4f0000c0
def int_2_bin(num):
    return '0' + bin(num)[2:] if num > 0 else '0'