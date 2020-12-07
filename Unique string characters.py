# https://www.codewars.com/kata/5a262cfb8f27f217f700000b/
def solve(a,b):
    sa = [letter for letter in a if not letter in b]
    sb = [letter for letter in b if not letter in a]
    return "".join(sa + sb)