# https://www.codewars.com/kata/5a61a846cadebf9738000076
def peak(arr):
    arr = [i for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i+1:])]
    return arr[0] if len(arr) > 0 else -1