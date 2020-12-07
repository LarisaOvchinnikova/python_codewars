#https://www.codewars.com/kata/5639bdcef2f9b06ce800005b/train/python
def make_string(s):
    return "".join([el[0] for el in s.split()])