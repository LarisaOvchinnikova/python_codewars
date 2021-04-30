# https://www.codewars.com/kata/57a03b8872292dd851000069
def nth_smallest(arr, n):
    return sorted(set(arr))[n-1] if 0 <= n-1 < len(set(arr)) else None