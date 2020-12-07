# https://www.codewars.com/kata/5340298112fa30e786000688/train/python

def twos_difference(lst):
    return sorted([(x, x + 2) for x in lst if (x + 2) in lst])