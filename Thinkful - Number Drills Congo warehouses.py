# https://www.codewars.com/kata/5862e7c63f8628a126000e18
def box_capacity(length, width, height):
    # convert to inches: 1 foot = 12 inches
    l = length * 12 // 16
    w = width * 12 // 16
    h = height * 12 // 16
    return l * w  * h