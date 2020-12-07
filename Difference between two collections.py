#https://www.codewars.com/kata/594093784aafb857f0000122
def diff(a, b):
    setA = set(a)
    setB = set(b)
    dif1 = setA - setB
    dif2 = setB - setA
    return sorted(list(dif1 | dif2))