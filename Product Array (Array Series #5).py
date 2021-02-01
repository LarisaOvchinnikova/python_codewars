# https://www.codewars.com/kata/5a905c2157c562994900009d
def product_array(numbers):
    p = 1
    for el in numbers:
        p *= el
    return [p / el for el in numbers]