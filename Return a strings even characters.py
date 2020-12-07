# https://www.codewars.com/kata/566044325f8fddc1c000002c/train/python
def even_chars(st):
    return [el for i, el in enumerate(st) if i % 2 != 0] if 1 < len(st) <= 100 else "invalid string"