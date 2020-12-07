https://www.codewars.com/kata/557341907fbf439911000022
def pattern(n):
    return "\n".join(["".join(map(str,list(range(n, i-1, -1)))) for i in range(n, 0, -1)])