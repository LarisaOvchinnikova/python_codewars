# https://www.codewars.com/kata/528d9adf0e03778b9e00067e
def mineLocation(field):
    return [[i, el.index(1)] for i,el in enumerate(field) if  1 in el][0]