https://www.codewars.com/kata/546e2562b03326a88e000020
def square_digits(num):
    a = [str(int(el)**2) for el in str(num)]
    return int("".join(a))