# https://www.codewars.com/kata/59859f435f5d18ede7000050
def word_to_bin(word):
    return [bin(ord(el))[2:].rjust(8, "0") for el in word]