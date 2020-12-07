# https://www.codewars.com/kata/5516ab668915478845000780
def reverse_by_center(s):
    i = len(s) // 2
    return s[i:] + s[:i] if len(s) % 2 ==0 else s[i+1:] + s[i]+ s[:i]