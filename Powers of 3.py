# https://www.codewars.com/kata/57be674b93687de78c0001d9/
def largest_power(n):
    k = 0
    while 3 ** k < n:
        k += 1
    return k - 1