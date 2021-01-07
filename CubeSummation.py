# https://www.codewars.com/kata/550e9fd127c656709400024d
def cube_sum(n, m):
    return sum([i ** 3 for i in range(min(n, m)+1, max(n, m) + 1)])