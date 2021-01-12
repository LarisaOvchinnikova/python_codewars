# https://www.codewars.com/kata/53e30ec0116393fe1a00060b
def unique(integers):
    arr = []
    for el in integers:
        if el not in arr:
            arr.append(el)
    return arr