https://www.codewars.com/kata/5a4b16435f08299c7000274f
def sum_square_even_root_odd(nums):
    return round(sum([el**2 if el %2 == 0 else el**0.5 for el in nums]), 2)