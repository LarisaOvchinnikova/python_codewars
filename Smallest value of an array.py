# https://www.codewars.com/kata/544a54fd18b8e06d240005c0
def find_smallest(numbers,to_return):
    return min(numbers) if to_return == 'value' else numbers.index(min(numbers))