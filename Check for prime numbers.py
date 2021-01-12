# https://www.codewars.com/kata/53daa9e5af55c184db00025f
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i  == 0:
            return False
    return True