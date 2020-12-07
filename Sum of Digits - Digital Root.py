https://www.codewars.com/kata/541c8630095125aba6000c00
def digital_root(n):
    while n > 9:
        s = 0
        for i in str(n):
            s += int(i)
        n = s
    return n