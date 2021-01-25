# https://www.codewars.com/kata/538948d4daea7dc4d200023f
def convert_bits(a, b):
    a = bin(a)[2:].rjust(32, "0")
    b = bin(b)[2:].rjust(32, "0")
    return sum([0 if a[i] == b[i] else 1 for i in range(len(a))])