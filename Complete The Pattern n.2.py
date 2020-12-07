# https://www.codewars.com/kata/55733d3ef7c43f8b0700007c/train/python
def pattern(n):
    arr = [list(range(n, i - 1, -1)) for i in range(1, n+1)]
    arr1 = []
    for el in arr:
        s = "".join([str(i) for i in el])
        arr1.append(s)
    return "\n".join(arr1)