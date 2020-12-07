# https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1

def capitalize(s,ind):
    return "".join([c.upper() if i in ind else c for i, c in enumerate(s)])