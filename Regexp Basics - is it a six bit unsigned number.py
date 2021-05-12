# https://www.codewars.com/kata/567e8dbb9b6f4da558000030

def six_bit_number(n):
    if (not n.isdigit() or len(n) > 1 and n[0] == '0'): return False
    return len(bin(int(n))[2:]) <= 6