https://www.codewars.com/kata/56eb16655250549e4b0013f4
from datetime import date, timedelta
def most_frequent_days(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): n = 366
    else: n = 365
    days = []
    start = date(year, 1, 1)
    for day in range(n):
        next_day = start + timedelta(day)
        name = next_day.strftime("%A")
        days.append(name)
    obj ={el:days.count(el) for el in days}
    res = [el[0] for el in obj.items() if el[1] == max(obj.values())]
    return res if res!=["Sunday", "Monday"] else ["Monday", "Sunday"]