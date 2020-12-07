https://www.codewars.com/kata/5648b12ce68d9daa6b000099

def number(bus_stops):
    return sum([el[0]-el[1] for el in bus_stops])