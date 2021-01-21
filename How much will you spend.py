# https://www.codewars.com/kata/585d7b4685151614190001fd
def get_total(costs, items, tax):
    price = sum([costs[el] for el in items if el in costs])
    return round(price + price * tax, 2)