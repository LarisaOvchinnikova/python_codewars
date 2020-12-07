#https://www.codewars.com/kata/5a8d1c82373c2e099d0000ac/train/python
def solve(st,a,b):
    return st[:a]+st[a:b+1][::-1]+st[b+1:]