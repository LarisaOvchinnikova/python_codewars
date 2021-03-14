# https://www.codewars.com/kata/590f5b4a7bbb3e246000007d
def comes_after(st, l):
    return "".join([st[i+1] for i in range(len(st)-1) if (st[i]).lower()==l.lower() and (st[i+1]).isalpha()])