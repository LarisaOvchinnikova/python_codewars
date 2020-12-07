https://www.codewars.com/kata/57f7b8271e3d9283300000b4
def even_or_odd(s):
    arr = [int(el) for el in list(s)]
    even = sum([el for el in arr if el % 2 == 0])
    odd = sum([el for el in arr if el % 2 != 0])
    return 'Even is greater than Odd' if even > odd else 'Odd is greater than Even' if odd > even else 'Even and Odd are the same'