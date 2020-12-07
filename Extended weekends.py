# https://www.codewars.com/kata/5be7f613f59e0355ee00000f/train/python
from datetime import date, timedelta
def solve(a,b):
    start = date(a, 1, 1)
    end = date(b, 12, 31)
    data = start
    dat = start
    while data < end:
        if data.weekday() == 4:
            dat = data
            break
        data = data + timedelta(1)
    count = 0
    dates = []
    while dat < end:
        if dat.day == 1  and dat.month in [1,3,5,7,8,10,12]:
            dates.append(dat.strftime("%b"))
            count += 1
        dat = dat + timedelta(weeks=1)

    return (dates[0], dates[-1], count)

# 2 case
from datetime import date


def solve(a, b):
    dates = []
    for year in range(a, b + 1):
        for month in 1, 3, 5, 7, 8, 10, 12:
            if date(year, month, 1).weekday() == 4:
                dates.append(date(year, month, 1).strftime("%b"))

    return (dates[0], dates[-1], len(dates))