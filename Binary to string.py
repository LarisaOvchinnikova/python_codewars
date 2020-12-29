# https://www.codewars.com/kata/5ab3495595df9ec78f0000b4
def binary_to_string(binary):
    return "".join([chr(int(el, 2)) for el in binary.split("0b") if el != ''])
