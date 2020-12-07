# https://www.codewars.com/kata/58e93b4706db4d24ee000096/train/python
def days_represented(trips):
    trip_dates = {}

    for trip in trips:
        for day in range(trip[0], trip[1] + 1):
            if day not in trip_dates:
                trip_dates[day] = 1
    return len(list(trip_dates))
