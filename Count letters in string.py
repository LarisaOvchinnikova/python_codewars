# https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d
def letter_count(s):
    return {letter:s.count(letter) for letter in s}