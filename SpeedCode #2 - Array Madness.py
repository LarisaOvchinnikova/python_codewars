# https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1
def array_madness(a,b):
    return sum([el**2 for el in a]) > sum([el**3 for el in b])