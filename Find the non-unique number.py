# https://www.codewars.com/kata/5b62031b97568072da0003db
def non_unique(lst):
    if lst == []: return []
    a = [int(el) if type(el)==str and el.isdigit() else float(el) if type(el)==str else el for el in lst]
    a = [[el, a.count(el)] for el in a if a.count(el) > 1]
    return a[0] if len(a)>0 else 'unique'