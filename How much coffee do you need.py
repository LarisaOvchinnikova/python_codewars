# https://www.codewars.com/kata/57de78848a8b8df8f10005b1/train/python
def how_much_coffee(events):
    events = [el for el in events if el.lower() in ["cat", "dog", "cw", "movie"]]
    s = sum([1 if el.islower() else 2 for el in events])
    return 'You need extra sleep' if s > 3 else s