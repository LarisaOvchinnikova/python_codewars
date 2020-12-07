https://www.codewars.com/kata/57ebdf944cde58f973000405
def reverser(s):
    return " ".join([el[::-1] for el in s.split(' ')])