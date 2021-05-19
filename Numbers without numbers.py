# https://www.codewars.com/kata/6098205ca76224000d62a2d0
def numbers_without_numbers():
    a = 'abcdef'
    return int("".join([str(a.index(el)) for el in "dcbfbedcf"]))