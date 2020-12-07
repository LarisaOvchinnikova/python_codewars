https://www.codewars.com/kata/54e6533c92449cc251001667
def unique_in_order(s):
    print(s)
    res = []
    for i, char in enumerate(s):
       if char != s[i-1] or i == 0:
           res.append(s[i])
    return res

# --- 2 case
def unique_in_order(s):
    return [char for i, char in enumerate(s) if char != s[i-1] or i == 0]