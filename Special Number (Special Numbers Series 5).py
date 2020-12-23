# https://www.codewars.com/kata/5a55f04be6be383a50000187
def special_number(number):
    return "Special!!" if len([el for el in str(number) if el in "012345"]) == len(str(number)) else "NOT!!"

# 2 case
def special_number(n):
    return "Special!!" if max(str(n)) <= "5" else "NOT!!"