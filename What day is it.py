# https://www.codewars.com/kata/5666bd1011beb6f768000073

from datetime import date
def day(dat):
    year = int(dat[:4])
    month = int(dat[4:6])
    day = int(dat[6:])
    d = date(year, month, day)
    return d.strftime("%A")
