# https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1
def solve(st):
    arr = [i+1 for i in range(0,len(st)//2) if st[:i+1] == st[-i-1:]]
    return max(arr) if len(arr)>0 else 0