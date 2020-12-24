# https://www.codewars.com/kata/5a4e3782880385ba68000018
def balanced_num(num):
    s = str(num)
    l = int(len(s) / 2)
    if len(s) % 2 == 0:
        s1 = sum([int(el) for el in s[: l-1]])
        s2 = sum([int(el) for el in s[l+1:]])
    else:
        s1 = sum([int(el) for el in s[: l]])
        s2 = sum([int(el) for el in s[l+1:]])
    return 'Balanced' if s1 == s2 else 'Not Balanced'