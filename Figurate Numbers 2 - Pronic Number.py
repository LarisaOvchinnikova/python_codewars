# https://www.codewars.com/kata/55b1e5c4cbe09e46b3000034
def is_pronic(n):
    for i in range(n + 1):
        if i * (i + 1) == n:
            return True
    return False