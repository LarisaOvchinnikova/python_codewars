# https://www.codewars.com/kata/55eea63119278d571d00006a/train/python
def next_id(arr):
    if arr == []:
        return 0
    r = [el for el in range(max(arr) + 1) if el not in arr]
    return r[0] if r else max(arr)+1