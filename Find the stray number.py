# https://www.codewars.com/kata/57f609022f4d534f05000024
def stray(arr):
    (a,b) = set(arr)
    return a if arr.count(a)==1 else b