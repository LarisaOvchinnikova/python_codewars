https://www.codewars.com/kata/58235a167a8cb37e1a0000db
def number_of_pairs(gloves):
    dct = {el:gloves.count(el) for el in gloves}
    return sum([el//2 for el in list(dct.values())])