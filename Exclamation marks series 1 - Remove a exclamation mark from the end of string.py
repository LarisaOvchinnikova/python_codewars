# https://www.codewars.com/kata/57faece99610ced690000165
def remove(s):
    return s[:-1] if s.endswith('!') else s