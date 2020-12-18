# https://www.codewars.com/kata/57f75cc397d62fc93d000059
def calc(x):
    arr = "".join([str(ord(el)) for el in x])
    count_7 = arr.count("7")
    return count_7 * 6