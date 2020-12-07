https://www.codewars.com/kata/58ae6ae22c3aaafc58000079
def permute_a_palindrome (input):
    return len([el for el in set(input) if input.count(el )% 2 != 0]) <= 1