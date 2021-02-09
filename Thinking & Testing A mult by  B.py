# https://www.codewars.com/kata/5a90c9ecb171012b47000077
def test_it(a, b):
    if a < 10 and b < 10:
        return a * b
    a = sum([int(el) for el in str(a)])
    b = sum([int(el) for el in str(b)])
    return a * b