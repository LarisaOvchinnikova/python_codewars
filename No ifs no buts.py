# https://www.codewars.com/kata/592915cc1fad49252f000006/
def no_ifs_no_buts(a, b):
    return {
        a > b: f"{a} is greater than {b}",
        a < b: f"{a} is smaller than {b}",
        a == b: f"{a} is equal to {b}"
    }[True]

#2 case
def no_ifs_no_buts(a, b):
    while a>b:
        return f"{a} is greater than {b}"
    while a<b:
        return f"{a} is smaller than {b}"
    return f"{a} is equal to {b}"