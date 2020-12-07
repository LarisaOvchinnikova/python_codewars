# https://www.codewars.com/kata/580435ab150cca22650001fb
def filter_lucky(lst):
    return [el for el in lst if str(el).count('7') > 0]