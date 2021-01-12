# https://www.codewars.com/kata/586d12f0aa042830910001d1
def remove_char(array):
    res = []
    for el in array:
        s = ''.join([c for i,c in enumerate(el) if c.isdigit()])
        res.append(f"${s}")
    return [el[:-2] + "." + el[-2:] for el in res]