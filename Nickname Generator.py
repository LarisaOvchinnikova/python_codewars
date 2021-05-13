# https://www.codewars.com/kata/593b1909e68ff627c9000186/
def nickname_generator(name):
    if len(name) < 4: return "Error: Name too short"
    if name[2] not in "aeiou":
        return name[0:3]
    return name[0:4]