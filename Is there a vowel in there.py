# https://www.codewars.com/kata/57cff961eca260b71900008f
def is_vow(a):
    code = { 97: "a", 101: "e", 105: "i", 111: "o", 117: "u"}
    return [code[el] if el in [97,101,105,111,117] else el for el in a]