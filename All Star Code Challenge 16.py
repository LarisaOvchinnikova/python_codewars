# https://www.codewars.com/kata/586566b773bd9cbe2b000013

def no_repeat(string):
    return [el for el in string if string.count(el) == 1][0]