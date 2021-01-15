# https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c
def switcher(arr):
    alph = "0zyxwvutsrqponmlkjihgfedcba!? ";
    return "".join([alph[int(el)] for el in arr])