# https://www.codewars.com/kata/595aa94353e43a8746000120
def find_deleted_number(arr, mixed_arr):
    return list(set(arr) - set(mixed_arr))[0] if list(set(arr) - set(mixed_arr)) != [] else 0

# 2 case
def find_deleted_number(arr, mixed_arr):
    return sum(arr) - sum(mixed_arr)