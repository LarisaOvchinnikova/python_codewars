# https://www.codewars.com/kata/558878ab7591c911a4000007
def pig_latin(s):
    vowels = "aeuio"
    non_al = [el for el in s if not el.isalpha()]
    if s == "" or len(non_al) > 0:
        return None
    s = s.lower()
    if s[0] in vowels:
        return s + "way"
    else:
        for el in s:
            if el not in vowels:
                s = s[1:] + s[:1]
            else:
                break
        return s + "ay"