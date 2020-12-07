# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
# 6 kyu
def find_nb(m):
    s = 0
    i = 1
    while s < m:
        s = s + i**3
        i += 1
    return i-1 if s == m else -1