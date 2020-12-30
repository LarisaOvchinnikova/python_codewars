# https://www.codewars.com/kata/5738f5ea9545204cec000155
def count_letters_and_digits(s):
    return len([el for el in s if el.isalnum()])