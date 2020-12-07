# https://www.codewars.com/kata/5511b2f550906349a70004e1
# YouTube: https://www.youtube.com/watch?v=1rwaAElTAlw
def last_digit(n1, n2):
    if n2 == 0: return 1
    last_n1 = n1 % 10
    if last_n1 in [1, 5, 6, 0]:
        return last_n1
    if last_n1 == 4:
        if n2 % 2 == 0:
            return 6
        else:
            return 4
    if last_n1 == 9:
        if n2 % 2 == 0:
            return 1
        else:
            return 9
    if last_n1 == 2:
        return [6,2,4,8][n2%4]
    if last_n1 == 3:
        return [1,3,9,7][n2%4]
    if last_n1 == 7:
        return [1,7,9,3][n2%4]
    if last_n1 == 8:
        return [6,8,4,2][n2%4]

#2 case
def last_digit(n1, n2):
    rules = {
    0: [0,0,0,0],
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6],
    5: [5,5,5,5],
    6: [6,6,6,6],
    7: [7,9,3,1],
    8: [8,4,2,6],
    9: [9,1,9,1],
  }
    rule = rules[n1 % 10]
    return 1 if n2 == 0 else rule[n2 % 4 - 1]