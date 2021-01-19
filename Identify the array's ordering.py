# https://www.codewars.com/kata/57f669477c9a2b1b9700022d
def order_type(arr):
    r = []
    for el in arr:
        if type(el) == str or type(el) == list:
            r.append(len(el))
        elif type(el) == int:
            r.append(len(str(el)))
    s = [el for el in r if el == r[0]]
    if len(s) == len(r): return "Constant"
    if r == sorted(r): return "Increasing"
    if r == sorted(r, reverse=True): return "Decreasing"
    return "Unsorted"