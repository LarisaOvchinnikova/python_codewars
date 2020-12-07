https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python
def row_weights(arr):
    s = sum([el for i, el in enumerate(arr) if i % 2 == 0])
    return s, sum(arr) - s

#2 case
def row_weights(arr):
    return sum(arr[::2]), sum(arr[1::2])