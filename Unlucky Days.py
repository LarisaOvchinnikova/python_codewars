#https://www.codewars.com/kata/56eb0be52caf798c630013c0
from datetime import datetime, date

def unlucky_days(year):
    return sum(date(year, m, 13).weekday() == 4 for m in range(1, 13))