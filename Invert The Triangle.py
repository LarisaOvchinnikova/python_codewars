#https://www.codewars.com/kata/5a224a15ee1aaef6e100005a
def invert_triangle(t):
    t = "\n".join(t.split("\n")[::-1])
    return t.replace(" ","*").replace("#", " ").replace("*", "#")