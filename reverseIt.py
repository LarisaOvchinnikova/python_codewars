# https://www.codewars.com/kata/557a2c136b19113912000010
def reverse_it(data):
    if type(data) in [int, str, float]:
        return type(data)(str(data)[::-1])
    return data