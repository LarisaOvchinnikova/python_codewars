# https://www.codewars.com/kata/58067088c27998b119000451/train/python
def reverse_factorial(num):
    if num <= 1:
        return f"1!"
    n = 0
    while num > 1:
        n += 1
        num = num / n

    return f"{n}!" if num == 1 else "None"