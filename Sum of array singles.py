https://www.codewars.com/kata/59f11118a5e129e591000134/train/python
def repeats(arr):
    return sum([el for el in arr if arr.count(el) == 1])