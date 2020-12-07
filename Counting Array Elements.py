# https://www.codewars.com/kata/5569b10074fe4a6715000054
def count(arr):
    return {el: arr.count(el) for el in arr}