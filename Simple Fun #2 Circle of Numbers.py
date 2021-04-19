# https://www.codewars.com/kata/58841cb52a077503c4000015
def circle_of_numbers(n, fst):
    m = n / 2
    if fst < m:
        return fst + m
    else:
        return fst - m