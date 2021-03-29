# https://www.codewars.com/kata/59a1ec603203e862bb00004f
def check_concatenated_sum(num, n):
    num = abs(num)
    return sum([int(el * n) for el in str(num)]) == num if n != 0 else False