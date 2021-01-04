# https://www.codewars.com/kata/56b8b0ae1d36bb86b2000eaa
def convert(time):
    t = time.strftime("%H:%M:%S,%f")
    return t[:-3]