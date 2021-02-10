# https://www.codewars.com/kata/57cf50a7eca2603de0000090
def move_ten(st):
    al = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for el in st:
        i = al.index(el)
        s += al[(i+10)%26]
    return s