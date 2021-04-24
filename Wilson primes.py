# https://www.codewars.com/kata/55dc4520094bbaf50e0000cb
def am_i_wilson(n):
#     if n <= 1: return False
#     fact = 1
#     for i in range(1,n):
#         fact = fact * i
#     return (fact + 1) % (n * n) == 0
#  The Wilson numbers are 1, 5, 13, 563, 5971, 558771, 1964215, 8121909, 12326713, 23025711, 26921605, 341569806, 399292158
    return n==5 or n==13 or n==563