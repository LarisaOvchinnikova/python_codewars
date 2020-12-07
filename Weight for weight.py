# https://www.codewars.com/kata/55c6126177c9441a570000cc/solutions/python

def order_weight(strng):
    arr = strng.split()
    arr_sum = []
    for el in arr:
        lst = list(el)
        s = sum([int(x) for x in lst])
        arr_sum.append((s, el))
    res = sorted(arr_sum)
    return " ".join(str(el[1]) for el in res)