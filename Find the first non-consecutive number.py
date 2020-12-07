#https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python
def first_non_consecutive(arr):
    for i in range(len(arr)-1):
        if arr[i] + 1 != arr[i + 1]:
            return arr[i + 1]
    return None