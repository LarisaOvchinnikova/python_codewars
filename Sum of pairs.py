https://www.codewars.com/kata/54d81488b981293527000c8f
def sum_pairs(lst, s):
    uniq = set()
    for i in lst:
        if s - i in uniq:
            return [s - i, i]
        uniq.add(i)

# 2 case:
def sum_pairs(ints, s):
    dct = {}
    for el in ints:
        if (s-el) in dct:
            return [s-el, el]
        else:
            dct[el] = 1