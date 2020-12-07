# https://www.codewars.com/kata/576bb71bbbcf0951d5000044
def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    sum = 0
    count = 0
    for el in arr:
        if el < 0:
            sum += el
        elif el > 0:
            count += 1
    return [count, sum]