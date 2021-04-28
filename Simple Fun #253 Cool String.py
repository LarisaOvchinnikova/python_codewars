# https://www.codewars.com/kata/590fd3220f05b4f1ad00007c
def cool_string(s):
    if not s.isalpha(): return False
    for i in range(len(s)-1):
        if s[i:i+2].islower() or s[i:i+2].isupper():
            return False
    return True