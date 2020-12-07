# https://www.codewars.com/kata/55968ab32cf633c3f8000008/train/python

def initials(name):
    name = name.split()
    return ".".join([el[0].upper() if i < len(name)-1 else el.title()  for i, el in enumerate(name)])

