https://www.codewars.com/kata/58f671ee5522a9c33800009b
def mult_implication(lst):
    if lst == []: return None
    res = True
    for el in lst:
        res = not res or el
    return res