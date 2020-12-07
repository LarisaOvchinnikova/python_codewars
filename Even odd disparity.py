https://www.codewars.com/kata/59c62f1bdcc40560a2000060/train/python
def solve(a):
    nums = [el for el in a if type(el) == int]
    return sum([1 if el % 2 == 0 else -1 for el in nums])