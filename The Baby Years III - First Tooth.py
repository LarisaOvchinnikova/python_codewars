# https://www.codewars.com/kata/5bcac5a01cbff756e900003e
def first_tooth(arr):
    a = []
    if len(arr) == 1: return 0
    a.append(arr[0] - arr[1])
    for i in range(1, len(arr)-1):
        a.append(arr[i] - arr[i-1] + arr[i] - arr[i+1])
    a.append(arr[-1] - arr[-2])
    if len(set(a)) == 1: return -1
    m = max(a)
    return a.index(m) if a.count(m) == 1 else -1