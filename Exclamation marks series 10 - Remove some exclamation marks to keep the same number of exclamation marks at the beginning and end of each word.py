# https://www.codewars.com/kata/57fb04649610ce369a0006b8
def remove(s):
    s = s.split(" ")
    arr = []
    for el in s:
        left = len(el) - len(el.lstrip("!"))
        right = len(el) - len(el.rstrip("!"))
        m = min(left, right)
        s = "!" * m + el.strip("!") + "!" * m
        arr.append(s)
    return " ".join(arr)