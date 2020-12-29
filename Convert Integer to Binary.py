https://www.codewars.com/kata/55606aeebf1f0305f900006f
def to_binary(n):
    return bin(((1 << 32) - 1) & n)[2:]