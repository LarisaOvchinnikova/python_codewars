# https://www.codewars.com/kata/5d49c93d089c6e000ff8428c
def save(sizes, hd):
    if sum(sizes) <= hd: return len(sizes)
    i = 0
    v = 0
    while v < hd:
        v += sizes[i]
        i += 1
    return i if v == hd else i - 1

# 2 case
def save(sizes, hd):
    return len([i for i in range(len(sizes)) if sum(sizes[:i+1]) <= hd])