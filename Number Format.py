# https://www.codewars.com/kata/565c4e1303a0a006d7000127
def number_format(n):
    sign = "" if n >=0 else "-"
    n = str(abs(n))
    if len(n) <= 3: return sign+n
    s = []
    while len(n)>0:
        s.append(n[-3:])
        n = n[:-3]
    return sign+",".join(s[::-1])