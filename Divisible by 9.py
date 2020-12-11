# https://www.codewars.com/kata/5f7b1a82be51af00105c82bd
def div_by_9(ns):
    return sum([int(el) for el in str(ns)]) % 9 == 0