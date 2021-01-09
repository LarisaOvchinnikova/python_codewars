# https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc
def split_by_value(k, elements):
    return [el for el in elements if el < k] + [el for el in elements if el >= k]