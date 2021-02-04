# https://www.codewars.com/kata/5296455e4fe0cdf2e000059f
def calculate(num1, op, num2):
    if op == '+':
        return num1 + num2;
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        return None if num2 == 0 else num1 / num2
    return None