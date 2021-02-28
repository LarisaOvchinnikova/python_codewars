# https://www.codewars.com/kata/603301b3ef32ea001c3395d0
def cinema(x, y):
    if x > 2 * y or y > 2 * x: return None
    return 'BGB'* (x - y) + 'BG' * (2 * y - x) if x >= y else 'GBG'* (y - x) + 'GB' * (2 * x - y)