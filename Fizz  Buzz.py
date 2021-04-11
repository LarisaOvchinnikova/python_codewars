# https://www.codewars.com/kata/51dda84f91f5b5608b0004cc
def solution(number):
    c3, c5, c15 = 0, 0, 0
    for i in range(1,number):
        if i % 15 == 0:
            c15 += 1
        if i % 3 == 0 and i % 5 != 0 :
            c3 += 1
        if i % 5 == 0 and i % 3 != 0 :
            c5 += 1
    return [c3,c5,c15]