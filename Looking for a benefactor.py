# https://www.codewars.com/kata/569b5cec755dd3534d00000f/
import math
def new_avg(arr, newavg):
    s = newavg * (len(arr) + 1)
    last = math.ceil(s - sum(arr))
    if last < 0:
        raise Exception
    return last
