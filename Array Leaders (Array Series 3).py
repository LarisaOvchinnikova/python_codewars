# https://www.codewars.com/kata/5a651865fd56cb55760000e0/train/python
def array_leaders(numbers):
    return [el for i, el in enumerate(numbers) if el > sum(numbers[i+1:])]