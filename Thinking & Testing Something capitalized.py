# https://www.codewars.com/kata/56d93f249c844788bc000002
def testit(s):
    return "" if s == "" else " ".join([el[:-1]+ el[-1].upper() for el in s.split()])