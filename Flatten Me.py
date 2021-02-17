# https://www.codewars.com/kata/55a5bef147d6be698b0000cd
def flatten_me(lst):
    res = []
    for el in lst:
        if type(el) != list:
            res.append(el)
        else:
            res.extend(el)
    return res