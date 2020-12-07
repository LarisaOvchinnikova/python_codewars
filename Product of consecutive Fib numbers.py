# 5 kyu
# https://www.codewars.com/kata/5541f58a944b85ce6d00006a
def productFib(prod):
    f1 = 0
    f2 = 1
    while f1 * f2 < prod:
        f1, f2 = f2, f1 + f2
    return [f1, f2, f1 * f2 == prod]