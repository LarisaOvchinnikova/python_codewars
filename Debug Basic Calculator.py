https://www.codewars.com/kata/56368f37d464c0a43c00007f/
def calculate(a, o, b):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "/" and b != 0:
        return a / b
    elif o == "*":
        return a * b
    else:
        return None