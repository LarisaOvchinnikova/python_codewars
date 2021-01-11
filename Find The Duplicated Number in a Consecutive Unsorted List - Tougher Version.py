# https://www.codewars.com/kata/558f0553803bc3c4720000af
def find_dup(arr):
    return [el for el in arr if arr.count(el) > 1][0]

#2 case
def find_dup(arr):
    return sum(arr) - sum(range(1, max(arr)+1))