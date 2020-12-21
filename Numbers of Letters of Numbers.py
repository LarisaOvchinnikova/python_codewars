# https://www.codewars.com/kata/599febdc3f64cd21d8000117
def numbers_of_letters(n):
    digits = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        }
    arr = []
    st = ''
    while st != "four":
        st = "".join([digits[el] for el in str(n)])
        arr.append(st)
        n = len(st)
    return arr