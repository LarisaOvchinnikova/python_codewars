# https://www.codewars.com/kata/5a97387e5ee396e70a00016d
def pofi(n):
    if n % 4 == 0: return "1"
    if n % 4 == 1: return 'i'
    if n % 4 == 2: return "-1"
    if n % 4 == 3: return "-i"