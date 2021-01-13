# https://www.codewars.com/kata/57faefc42b531482d5000123
def remove(s):
    t = s.rstrip("!")
    count = len(s) - len(t)
    return s.replace("!", "") + "!" * count