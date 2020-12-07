# https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python
def race(v1, v2, g):
    if v1 >= v2:
        return None
    t = g /(v2 - v1)
    time = t * 3600
    hour = time // 3600
    min = time % 3600 // 60
    sec = time % 60
    return [int(hour), int(min), int(sec)]