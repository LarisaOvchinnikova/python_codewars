# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(arr):
    s = [0 if el % 2 == 0 else 1 for el in arr]
    if s.count(1) > s.count(0):
        return arr[s.index(0)]
    else:
        return arr[s.index(1)]