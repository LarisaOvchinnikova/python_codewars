# https://www.codewars.com/kata/58845a92bd573378f4000035
def swap_adjacent_bits(n):
    b = bin(n)[2:].rjust(32, "0")
    b = "".join([b[i+1]+b[i]for i in range(0, len(b)-1,2)])
    return int(b,2)