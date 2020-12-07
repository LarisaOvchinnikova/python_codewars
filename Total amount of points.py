# https://www.codewars.com/kata/5bb904724c47249b10000131
def points(games):
    s = 0
    for el in games:
        if int(el[0]) > int(el[2]):
            s += 3
        elif int(el[0]) == int(el[2]):
            s += 1
    return s
# ----2 case
def points(games):
    s = sum([3 if el[0]>el[2] else 0 if el[0]<el[2] else 1 for el in games])
    return s