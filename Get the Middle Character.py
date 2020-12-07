https://www.codewars.com/kata/56747fd5cb988479af000028/python
def get_middle(s):
    n = len(s) // 2
    if len(s) % 2 == 0:
        return s[n-1:n+1]
    else:
        return s[n]