# https://www.codewars.com/kata/5bb3e299484fcd5dbb002912
def pyramid(balls):
    n = 0
    while balls > 0:
        n += 1
        balls = balls - n
    return  n if balls == 0 else n - 1