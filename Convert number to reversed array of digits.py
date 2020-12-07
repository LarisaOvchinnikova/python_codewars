https://www.codewars.com/kata/5583090cbe83f4fd8c000051
def digitize(n):
    lst = list(str(n)[::-1])
    res = [int(el) for el in lst]
    return res
print(digitize(35231))