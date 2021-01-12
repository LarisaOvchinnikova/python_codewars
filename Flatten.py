# https://www.codewars.com/kata/5250a89b1625e5decd000413
def flatten(lst):
    arr = []
    for el in lst:
        arr.extend(el) if type(el) == list else arr.append(el)
    return arr