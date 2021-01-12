# https://www.codewars.com/kata/5884b6550785f7c58f000047
def group(arr):
    res = []
    for el in arr:
        if [el] * arr.count(el) not in res:
            res.append([el] * arr.count(el))
    return res