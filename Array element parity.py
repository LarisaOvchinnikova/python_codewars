# https://www.codewars.com/kata/5a092d9e46d843b9db000064/train/python
def solve(arr):
    return [el for el in arr if arr.count(-el) == 0][0]
# 2 case
def solve(arr):
    return sum(set(arr))