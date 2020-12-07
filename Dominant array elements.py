# https://www.codewars.com/kata/5a04133e32b8b998dc000089/solutions/python
def solve(arr):
    return [el for i, el in enumerate(arr) if i < len(arr)-1 and el > max(arr[i+1:])]+ arr[-1:]