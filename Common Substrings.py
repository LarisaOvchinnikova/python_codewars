# https://www.codewars.com/kata/5669a5113c8ebf16ed00004c
def substring_test(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    for i in range(len(s1)-2):
        if s1[i:i+2] in s2:
                return True
    return False