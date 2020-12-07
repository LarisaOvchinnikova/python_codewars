# https://www.codewars.com/kata/57a37f3cbb99449513000cd8
def get_number_from_string(string):
    return int("".join([el for el in string if el.isdigit()]))