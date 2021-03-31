# https://www.codewars.com/kata/59887207635904314100007b
def closest(lst):
    m = min([abs(el) for el in lst])
    count = 0
    for el in set(lst):
        if abs(el)== m:
            count +=1
            x = el
    return x if count == 1 else None