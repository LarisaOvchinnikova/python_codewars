# https://www.codewars.com/kata/5979d27b630baf1509000064
def square_root_me(num):
    n = 0
    odd = 1
    while num >=1:
        num -= odd
        odd += 2
        n+=1
    return n