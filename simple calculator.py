# https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python
def calculator(a,b,op):
    if type(a) != int or type(b) != int:
        return 'unknown value'
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return 'unknown value'