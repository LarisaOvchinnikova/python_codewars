# https://www.codewars.com/kata/578fdcfc75ffd1112c0001a1
def bin_rota(arr):
    arr = [el if i % 2 == 0 else el[::-1] for i, el in enumerate(arr)]
    res = []
    for el in arr:
        res.extend(el)
    return res