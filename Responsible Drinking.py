https://www.codewars.com/kata/5aee86c5783bb432cd000018/train/python

def hydrate(drink):
    drink = drink.split()
    s = sum([int(el) for el in drink if el.isdigit()])
    return "1 glass of water" if s == 1 else f"{s} glasses of water"