https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
def accum(s):
    s1 = ""
    for i in range(len(s)):
        s1 = s1 + s[i].upper() + s[i].lower() * i + "-"
    return s1[:-1]

# === 2 case
def accum(s):
    return '-'.join([c.upper() + c.lower() * i for i, c in enumerate(s)])