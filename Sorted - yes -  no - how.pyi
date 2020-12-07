# https://www.codewars.com/kata/580a4734d6df748060000045
def is_sorted_and_how(arr):
    ar = arr[::]
    return 'yes, ascending' if arr == sorted(ar) else 'yes, descending' if arr == sorted(ar,reverse=True) else "no"