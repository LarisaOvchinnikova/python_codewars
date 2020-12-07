# https://www.codewars.com/kata/576b93db1129fcf2200001e6
def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0
    return sum(arr) - max(arr) - min(arr)