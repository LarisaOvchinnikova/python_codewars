# https://www.codewars.com/kata/54da5a58ea159efa38000836
# Given an array, find the integer that appears an odd number of times.

def find_it(seq):
    c = [el for el in seq if seq.count(el) % 2 != 0]
    arr = list(set(c))
    return arr[0]

# --- 2 case
def find_it(seq):
    return [el for el in seq if seq.count(el) % 2 != 0][0]
