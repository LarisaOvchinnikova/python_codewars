#https://www.codewars.com/kata/5a07e5b7ffe75fd049000051/train/python
def get_first(element):
    return element[0]

def sorter(textbooks):
    lst = [(el.lower(), el) for el in textbooks]
    lst1 = sorted(lst, key=get_first)
    return [el[1] for el in lst1]

def sorter(textbooks):
    return sorted(textbooks, key=str.lower)

def sorter(textbooks):
    return sorted(textbooks, key=lambda x: x.lower())