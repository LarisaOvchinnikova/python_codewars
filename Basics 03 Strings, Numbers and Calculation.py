# https://www.codewars.com/kata/56b5dc75d362eac53d000bc8/train/python
def calculate_string(st):
    s = ""
    for el in st:
        if el.isdigit() or el in ".+-*/":
            s = s + el
    for i, el in enumerate(s):
        if el in "+-*/":
            oper = i
    num1 = float(s[:oper])
    num2 = float(s[oper+1:])
    op = s[oper]
    if op == "+":
        res = num1 + num2
    elif op == "-":
        res = num1 - num2
    elif op == "*":
        res = num1 * num2
    elif op == "/":
        res = num1 / num2
    return str(round(res))

# 2 case:
def calculate_string(st):
    arr = [el for el in st if el.isnumeric() or el in '.+-*/']
    return str(round(eval("".join(arr))))