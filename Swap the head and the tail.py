# https://www.codewars.com/kata/5a34f087c5e28462d9000082
def swap_head_tail(arr):
    if len(arr) % 2 == 0:
        p1 = arr[:len(arr)//2]
        p2 = arr[len(arr)//2:]
        return p2+p1
    else:
        p1 = arr[:len(arr)//2]
        p2 = arr[len(arr)//2+1:]
        return p2 + [arr[len(arr)//2]] + p1

#2 case
def swap_head_tail(arr):
    i = len(arr) // 2
    return arr[-i:] + arr[i:-i] + arr[:i]