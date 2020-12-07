# https://www.codewars.com/kata/580751a40b5a777a200000a1
def vowel_one(s):
    a = ""
    s = s.lower()
    for el in s:
        if el in "aeiou":
            a = a + "1"
        else:
            a = a + "0"
    return a