# https://www.codewars.com/kata/55749101ae1cf7673800003e
def pattern(n):
    return "\n".join([str(i)*i for i in range(2, n+1, 2)])