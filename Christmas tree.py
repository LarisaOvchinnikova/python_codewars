# https://www.codewars.com/kata/52755006cc238fcae70000ed
def christmas_tree(height):
    width = height * 2 - 1
    s = []
    for i in range(1, width+1, 2):
        s.append(("*" * i).center(width))
    return "\n".join(s)