https://www.codewars.com/kata/59f08f89a5e129c543000069
def dup(arr):
    res = []
    s = ''
    for el in arr:
        s = el[0]
        for i in range(len(el)):
            if s[-1] != el[i]:
                s += el[i]
        res.append(s)
    return res