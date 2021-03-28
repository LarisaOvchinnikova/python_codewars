# https://www.codewars.com/kata/5375f921003bf62192000746
def change(s):
    if len(s) <= 3: return s
    return s[0] + str(len(s)-2) + s[-1]
def abbreviate(s):
    seps = [el for el in s if not el.isalpha()]
    s1 = "".join([el if el not in seps else "*" for el in s ])
    s2 = [change(el) for el in s1.split("*")]
    res = ''
    for i in range(len(seps)):
        res += s2[i] + seps[i]
    res+=s2[-1]
    return res