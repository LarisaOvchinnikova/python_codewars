https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python
import math
def what_century(year):
    year = int(year)
    century = math.ceil(year / 100)
    last = century % 10
    ending = "th"
    if century < 10 or century > 20:
        if last == 1:
            ending = "st"
        elif last == 2:
            ending = "nd"
        elif last == 3:
            ending = "rd"
    return f"{century}{ending}"