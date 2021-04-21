# https://www.codewars.com/kata/5865a75da5f19147370000c7
def add_arrays(a, b):
    if len(a) != len(b):
        raise Exception
    return [a[i] + b[i] for i in range(len(a))]

# 2 case
def add_arrays(a, b):
    if len(a) != len(b):
        raise ValueError
    return [a[i] + b[i] for i in range(len(a))]