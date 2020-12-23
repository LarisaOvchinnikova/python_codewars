# https://www.codewars.com/kata/5a4d303f880385399b000001
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def strong_num(number):
    return 'STRONG!!!!' if sum([factorial(int(el)) for el in str(number)]) == number else 'Not Strong !!'
