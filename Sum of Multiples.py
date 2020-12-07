# https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python
def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return "INVALID";
    return sum(list(range(n, m, n)))