https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4
def least_larger(a, i):
    b = sorted([el for el in a if el > a[i]])
    return a.index(b[0]) if len(b)>0 else -1