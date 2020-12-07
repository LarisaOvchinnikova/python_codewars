#https://www.codewars.com/kata/5413759479ba273f8100003d/train/python
def reverse(lst):
    arr = list()
    for el in lst:
        arr.insert(0, el)
    return arr