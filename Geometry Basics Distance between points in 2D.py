# https://www.codewars.com/kata/58dced7b702b805b200000be/train/python
def distance_between_points(a, b):
    return round((((b.x - a.x) ** 2 + (b.y - a.y)**2) ** 0.5),6)