# https://www.codewars.com/kata/5f47e79e18330d001a195b55/train/python
def base_finder(seq):
    return int(max(list("".join(seq)))) + 1