#https://www.codewars.com/kata/5ce399e0047a45001c853c2b
def parts_sums(ls):
    s = sum(ls)
    res = [s]
    for el in ls:
        s = s - el
        res.append(s)
    return res