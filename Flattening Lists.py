# https://www.codewars.com/kata/54474afb46324f45190000a5
def flatten(l):
    arr = []
    for el in l:
        arr.extend(el)
    return arr