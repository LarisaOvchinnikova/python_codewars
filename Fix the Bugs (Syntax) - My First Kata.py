# https://www.codewars.com/kata/56aed32a154d33a1f3000018
def my_first_kata(a,b):
    if type(a) != int or type(b) != int:
        return False
    else:
        return a % b + b % a