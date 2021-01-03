# https://www.codewars.com/kata/55ed875819ae85ca8b00005c
def multiply_and_filter(seq, multiplier):
    return [el * multiplier for el in seq if type(el) in [int,float]]