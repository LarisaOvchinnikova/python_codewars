# https://www.codewars.com/kata/55caef80d691f65cb6000040
def geometric_sequence_elements(a, r, n):
    arr = []
    for i in range(n):
        arr.append(a)
        a *= r
    return ", ".join([str(el) for el in arr])

# 2 case
def geometric_sequence_elements(a, r, n):
    return ', '.join([str(a * r ** i) for i in range(n)])