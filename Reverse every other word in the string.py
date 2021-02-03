# https://www.codewars.com/kata/58d76854024c72c3e20000de
def reverse_alternate(s):
    return " ".join([el if i % 2 == 0 else el[::-1] for i, el in enumerate(s.split())])