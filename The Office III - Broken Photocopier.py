# https://www.codewars.com/kata/57ed56657b45ef922300002b
def broken(inp):
    s = ''
    for el in inp:
        s += "1" if el == "0" else "0"
    return s

# 2case
def broken(inp):
    return "".join(["0" if el == "1" else "1" for el in inp])