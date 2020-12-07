#https://www.codewars.com/kata/596f6385e7cd727fff0000d6/train/python
def avg_array(arrs):
    av = []
    l = len(arrs[0])
    for j in range(l):
        s = 0
        for i in range(len(arrs)):
            s += arrs[i][j]
        s = s / len(arrs)
        av.append(s)