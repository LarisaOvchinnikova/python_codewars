# https://www.codewars.com/kata/55a58505cb237a076100004a
def find_2nd_largest(arr):
    arr = sorted(set([el for el in arr if type(el)== int]))[::-1]
    return arr[1] if len(arr) > 1 else None