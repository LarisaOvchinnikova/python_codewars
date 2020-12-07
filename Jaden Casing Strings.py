# https://www.codewars.com/kata/5390bac347d09b7da40006f6/solutions/python
def to_jaden_case(s):
    return " ".join([el.capitalize() for el in s.split()])