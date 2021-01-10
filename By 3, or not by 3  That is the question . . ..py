# https://www.codewars.com/kata/59f7fc109f0e86d705000043
def divisible_by_three(st):
    s = sum([int(el) for el in list(st)])
    p = 0
    while p < s:
        p += 3
    return p == s