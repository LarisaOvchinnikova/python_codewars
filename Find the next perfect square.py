# https://www.codewars.com/kata/56269eb78ad2e4ced1000013
def isPerfect(n):
    return (n ** 0.5).is_integer()


def find_next_square(sq):
    if isPerfect(sq):
        x = sq + 1
        while not isPerfect(x):
            x += 1
        return x
    else:
        return -1

# ---2 case
def find_next_square(n):
    if (n ** 0.5).is_integer():
        return ((n ** 0.5) + 1) ** 2
    else:
        return -1