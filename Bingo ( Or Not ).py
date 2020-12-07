# https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145/train/python

def bingo(array):
    return "WIN" if len([1 for el in [2, 7, 9, 14, 15] if el in array]) == 5 else "LOSE"




print(bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]))