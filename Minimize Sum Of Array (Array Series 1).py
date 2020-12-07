# https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/
def min_sum(arr):
    arr = sorted(arr)
    return sum([arr[i]*arr[-i -1] for i in range(0,len(arr)//2)])