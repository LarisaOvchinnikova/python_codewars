https://www.codewars.com/kata/523f5d21c841566fde000009
def array_diff(a, b):
    return [el for el in a if b.count(el) == 0]


# 2 case
def array_diff(a, b):
    return [el for el in a if not el in b]