# https://www.codewars.com/kata/58fd52b59a9f65c398000096
def min_and_max(l, d, x):
    res = []
    for el in range(l, d+1):
        s = sum([int(elem) for elem in str(el)])
        if s == x:
            res.append(el)
    return [min(res), max(res)]