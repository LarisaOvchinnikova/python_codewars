# https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5
def reverse_number(n):
    sign = -1 if n < 0 else 1
    return int(str(abs(n))[::-1]) * sig