https://www.codewars.com/kata/5a9e86705ee396d6be000091
# 1 case (list comprehension)
def check_three_and_two(array):
    return len([el for el in array if array.count(el) == 2 or array.count(el) == 3 ]) == len(array)

# 2 case: (dictionary)
def check_three_and_two(array):
    return sorted({el:array.count(el) for el in array}.values()) == [2,3]

# 3 case: (set)
def check_three_and_two(array):
    return {array.count(el) for el in array} == {2,3}