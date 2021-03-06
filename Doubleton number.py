# https://www.codewars.com/kata/604287495a72ae00131685c7
def is_dual(num):
    return len(set(str(num))) == 2

def dual(num):
    num += 1
    while not is_dual(num):
        num += 1
    return num