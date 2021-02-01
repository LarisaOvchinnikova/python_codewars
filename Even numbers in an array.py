# https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c
def even_numbers(arr,n):
    return [el for el in arr if el % 2 == 0][-n:]