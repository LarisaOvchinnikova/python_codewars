# https://www.codewars.com/kata/58845748bd5733f1b300001f
def range_bit_count(a, b):
    return sum([(bin(i)[2:]).count('1') for i in range (a, b+1)])