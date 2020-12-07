# https://www.codewars.com/kata/5ce6728c939bf80029988b57/train/python
def solve(st):
    return "".join(sorted(list(st))) in 'abcdefghijklmnopqrstuvwxyz'
