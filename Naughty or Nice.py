# https://www.codewars.com/kata/52a6b34e43c2484ac10000cd/
def get_nice_names(people):
    return [el['name'] for el in people if el['was_nice']]

def get_naughty_names(people):
    return [el['name'] for el in people if not el['was_nice']]