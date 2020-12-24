# https://www.codewars.com/kata/5a53a17bfd56cb9c14000003
def disarium_number(num):
    return "Disarium !!" if num == sum([int(el) ** (i+1) for i, el in enumerate(str(num))]) else "Not !!"