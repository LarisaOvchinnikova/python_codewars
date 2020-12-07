#https://www.codewars.com/kata/5a090c4e697598d0b9000004
def solve(arr):
    arr = sorted(arr)
    print(arr)
    res = []
    while len(arr)>0:
        res.append(arr[-1])
        arr.pop()
        if len(arr) == 0:
            break
        else:
            res.append(arr[0])
            del arr[0]
    return res

#2 case
def solve(arr):
    arr = sorted(arr)
    res = []
    for i in range(0, len(arr)//2):
        res.append(arr[-i-1])
        res.append(arr[i])
    if len(arr) % 2 != 0:
        res.append(arr[len(arr)//2])
    return res

# 3 case
def solve(arr):
    arr = sorted(arr)
    res = []
    while len(arr)>1:
        res.append(arr[-1])
        arr.pop()
        res.append(arr[0])
        arr.pop(0)
    if len(arr) > 0:
        res.append(arr[0])
    return res
