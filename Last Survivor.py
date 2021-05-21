# https://www.codewars.com/kata/609eee71109f860006c377d1
def last_survivor(s, coords):
    for i in coords:
        s = s[:i] + s[i+1:]
    return s