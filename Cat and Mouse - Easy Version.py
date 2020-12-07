# https://www.codewars.com/kata/57ee24e17b45eff6d6000164
def cat_mouse(x):
    return "Escaped!" if abs(x.find("C") - x.find("m")) > 4 else "Caught!"

# 2 case
def cat_mouse(x):
    return "Escaped!" if x.count('.') > 3 else "Caught!"