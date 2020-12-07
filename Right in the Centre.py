https://www.codewars.com/kata/5f5da7a415fbdc0001ae3c69/
def is_in_middle(s):
    mid = len(s) // 2
    return s[mid-1:mid+2]=="abc" if len(s)%2!=0 else s[mid-2:mid+1]=="abc" or s[mid-1:mid+2]=="abc"