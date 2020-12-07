# https://www.codewars.com/kata/5dd259444228280032b1ed2a
def solve(s,g):
    for x in range(g, s-g+1, g):
        if (s - x) % g == 0:
            return x, s-x
    return -1


#2 case
def solve(s,g):
    return (g, s-g) if (s-g) % g == 0 else -1