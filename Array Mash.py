# https://www.codewars.com/kata/582642b1083e12521f0000da
def array_mash(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i])
        res.append(b[i])
    return res

lst = [1,2,3]
print(lst)