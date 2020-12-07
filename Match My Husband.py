https://www.codewars.com/kata/5750699bcac40b3ed80001ca
def match(usefulness, months):
    s = sum(usefulness)
    r = 100
    for month in range(0, months+1):
        if s >= r:
            return "Match!"
        r -= 0.15 * r
    return "No match!"