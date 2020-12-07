# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0
def ct(s):
    s = s.lower()
    a = 'abcdefghijklmnopqrstuvwxyz'
    return len([el for i,el in enumerate(s) if i == a.find(el)])
def solve(arr):
    return [ct(el) for el in arr]