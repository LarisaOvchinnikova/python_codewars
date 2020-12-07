https://www.codewars.com/kata/5840586b5225616069000001
def highest_value(a, b):
    a1 = sum([ord(el) for el in a])
    b1 = sum([ord(el) for el in b])
    return a if a1 >= b1 else b