#https://www.codewars.com/kata/5f55ecd770692e001484af7d
def mirror(list):
    l = sorted(list)
    l1 = l[::-1][1:]
    return l+l1