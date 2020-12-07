# https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/python

def in_asc_order(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def in_asc_order(arr):
    return arr == sorted(arr)