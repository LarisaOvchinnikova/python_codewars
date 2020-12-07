# https://www.codewars.com/kata/575fa9afee048b293e000287
def how_much_water(water, load, clothes):
    return 'Too much clothes' if clothes > 2 * load else 'Not enough clothes' if clothes < load else round(water * 1.1 ** (clothes-load), 2)