# https://www.codewars.com/kata/598f76a44f613e0e0b000026
def sum_of_integers_in_string(s):
    s = "".join([el if el.isdigit() else " " for el in s])
    return sum([int(el) for el in s.split(" ") if el.isdigit()])