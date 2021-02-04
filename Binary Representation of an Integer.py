# https://www.codewars.com/kata/5a5f3034cadebf76db000023
def show_bits(n):
    if n < 0:
        arr = list(bin(((1 << 32) - 1) & n)[2:])
    else:
        arr = list(bin(n)[2:].rjust(32, "0"))
    return [int(el) for el in arr]