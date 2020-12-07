# https://www.codewars.com/kata/55b051fac50a3292a9000025
def filter_string(string):
    return int("".join([el for el in string if el.isdigit()]))