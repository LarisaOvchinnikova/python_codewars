https://www.codewars.com/kata/57faa6ff9610ce181b000028


def crap(garden, bags, cap):
    c = 0
    for el in garden:
        for e in el:
            if e == "@":
                c += 1
            if e == "D":
                return "Dog!!"

    return "Clean" if c <= bags * cap else "Cr@p"