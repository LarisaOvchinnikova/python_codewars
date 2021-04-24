# https://www.codewars.com/kata/5901f361927288d961000013
def product(numbers):
    if not numbers: return None
    p = 1
    for el in numbers:
        p *= el
    return p