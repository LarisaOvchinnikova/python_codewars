# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
def valid_parentheses(str):
    count = 0
    for el in str:
        if el == "(":
            count += 1
        elif el == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0