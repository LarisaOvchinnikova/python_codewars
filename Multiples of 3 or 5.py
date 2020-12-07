# https://www.codewars.com/kata/514b92a657cdc65150000006
def solution(number):
    return sum([el for el in range(number) if el % 3 == 0 or el % 5 == 0])