#https://www.codewars.com/kata/58f8b35fda19c0c79400020f/train/python
def all_non_consecutive(arr):
    res = []
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            res.append({"i": i, "n": arr[i]})
    return res

# 2 case
def all_non_consecutive(arr):
    return [{"i": i, "n": arr[i]} for i in range(1, len(arr)) if arr[i] != arr[i-1] + 1]