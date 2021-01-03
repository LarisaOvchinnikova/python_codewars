# https://www.codewars.com/kata/586bca7fa44cfc833e00005c
def create_array_of_tiers(n):
    n = str(n)
    return [n[:i+1] for i in range(len(n))]