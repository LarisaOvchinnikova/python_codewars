# https://www.codewars.com/kata/57efab9acba9daa4d1000b30
def bald(s):
    n = s.count('/')
    s = s.replace("/", "-")
    name = ''
    if n == 0: name = "Clean!"
    elif n == 1: name = "Unicorn!"
    elif n == 2 : name = "Homer!"
    elif n < 6: name = "Careless!"
    else: name = "Hobo!"
    return [s, name]