# https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf
def cat_mouse(x, j):
    if x.find("D") == -1 or x.find("C") == -1 or x.find("m") == -1:
        return "boring without all three"
    else:
        dog = x.index("D")
        cat = x.index("C")
        mouse = x.index("m")

    if abs(cat - mouse) <= j:
        if (cat < dog < mouse or mouse < dog < cat):
            return "Protected!"
        else:
            return "Caught!"
    else:
        return "Escaped!"