# https://www.codewars.com/kata/5574940eae1cf7d520000076
def pattern(n):
    return "\n".join([str(i)*i for i in range(1, n+1, 2)])