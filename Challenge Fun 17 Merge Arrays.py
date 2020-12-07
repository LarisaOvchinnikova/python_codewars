# https://www.codewars.com/kata/58b665c891e710a3ec00003f
def merge_arrays(a, b):
    arr = []
    for el in a:
        if b.count(el) == 0 or a.count(el) == b.count(el):
            arr.append(el)
    for el in b:
        if a.count(el) == 0 or a.count(el) == b.count(el):
            arr.append(el)
    return sorted(set(arr))