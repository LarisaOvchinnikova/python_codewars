# https://www.codewars.com/kata/567e8f7b4096f2b4b1000005
def eight_bit_number(n):
    return n in [str(i) for i in range(256)]