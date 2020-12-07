# https://www.codewars.com/kata/5a07e5b7ffe75fd049000051/train/python
def sorter(textbooks):
    lst = sorted([(el.lower(), el) for el in textbooks])
    return [el[1] for el in lst]
