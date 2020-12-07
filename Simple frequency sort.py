https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc


def solve(arr):
    obj = {};
    for el in arr:
        if el in obj:
            obj[el] += 1
        else:
            obj[el] = 1
    arr = sorted(arr)
    return sorted(arr, key=lambda el: obj[el], reverse=True)
