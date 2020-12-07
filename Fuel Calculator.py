#https://www.codewars.com/kata/57b58827d2a31c57720012e8/train/python
def fuel_price(litres, price_per_liter):
    if litres < 2:
        price = litres * price_per_liter;
    elif litres < 4:
        price = litres * (price_per_liter - 0.05);
    elif litres < 6:
        price = litres * (price_per_liter - 0.10);
    elif litres < 8:
        price = litres * (price_per_liter - 0.15);
    elif litres < 10:
        price = litres * (price_per_liter - 0.20);
    else:
        price = litres * (price_per_liter - 0.25);
    return round(price, 2)

#2 casee
def fuel_price(litres, price_per_litre):
    for i in range(2, 11, 2):
        if litres >= i: price_per_litre -= 0.05
    return round(litres * price_per_litre, 2)