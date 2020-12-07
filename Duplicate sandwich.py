https://www.codewars.com/kata/5f8a15c06dbd530016be0c19


def duplicate_sandwich(arr):
    dupl = [i for i, el in enumerate(arr) if arr.count(el) == 2]
    return arr[dupl[0] + 1: dupl[1]]
