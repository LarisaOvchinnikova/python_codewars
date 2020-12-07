# Sum of positive
# https://www.codewars.com/kata/5715eaedb436cf5606000381

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum = sum + i
    return sum

# 2 case
def positive_sum(arr):
    return sum([el for el in arr if el > 0])