# https://www.codewars.com/kata/5ac54bcbb925d9b437000001
def find_middle(string):
    if type(string)!= str: return -1
    s = [int(el) for el in string if el.isdigit()]
    if s == []: return -1
    p = 1
    for el in s:
        p *= el
    p = str(p)
    mid = len(p) // 2
    return int(p[mid]) if len(p) % 2 != 0 else int(p[mid-1:mid+1])