# https://www.codewars.com/kata/57faf7275c991027af000679
def remove(s, n):
    for i in range(n):
        s = s.replace("!", '', 1)
    return s