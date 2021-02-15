# https://www.codewars.com/kata/588a556d4b9a4bd09a000d1b
def move_zeroes(*args):
    return sorted([el for el in args if el != 0]) + [0] * args.count(0)