# https://www.codewars.com/kata/58279e13c983ca4a2a00002a
def greet_developers(lst):
    for el in lst:
        el['greeting'] = f"Hi {el['firstName']}, what do you like the most about {el['language']}?"
    return lst