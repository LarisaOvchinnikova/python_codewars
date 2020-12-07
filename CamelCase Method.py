#https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python
def camel_case(string):
    return "".join([el.title() for el in string.split()])

# 2 case
def camel_case(string):
    return string.title().replace(" ", "")