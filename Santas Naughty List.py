# Santa's Naughty List
# https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef/train/python
def find_children(santas_list, children):
    return sorted([el for el in santas_list if el in children])
