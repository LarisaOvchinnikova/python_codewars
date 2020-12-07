# https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python
def add_length(s):
    return [f"{el } {len(el)}" for el in s.split()]