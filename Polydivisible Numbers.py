# https://www.codewars.com/kata/5e4217e476126b000170489b
def polydivisible(x):
    s = str(x)
    for i in range(1, len(s)+1):
        if int(s[:i]) % i != 0:
            return False
    return True