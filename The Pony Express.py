# https://www.codewars.com/kata/5b18e9e06aefb52e1d0001e9
def riders(st):
    s = 0
    count = 1
    i = 0
    while i < len(st):
        s += st[i]
        if s > 100:
            count += 1
            s = 0
        else:
            i += 1
    return count