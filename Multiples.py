#https://www.codewars.com/kata/55a8a36703fe4c45ed00005b
def multiple(x):
    if x % 3 == 0 and x % 5 == 0:
        return "BangBoom"
    elif x % 3 == 0:
        return "Bang"
    elif x % 5 == 0:
        return "Boom"
    else:
        return "Miss"

# 2 case
def multiple(x):
    return "Bang" * (x % 3 == 0) + "Boom" * (x % 5 == 0) or "Miss"