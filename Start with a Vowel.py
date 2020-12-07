#https://www.codewars.com/kata/5a02e9c19f8e2dbd50000167
def vowel_start(st):
    s = st.lower().replace(" ", "")
    s = "".join([el for el in s if el.isalnum()])
    if s == "": return ""
    vowels = "aeuio"
    res = []
    word = s[0]
    for i in range(1,len(s)):
        if s[i] not in vowels:
            word += s[i]
        else:
            res.append(word)
            word = s[i]
    res.append(word)
    return " ".join(res)
#2 case
def vowel_start(st):
    s = st.lower()
    s = "".join([el for el in s if el.isalnum()])
    s = s.replace("a", " a").replace("o", " o").replace("e", " e").replace("i", " i").replace("u", " u")
    return " ".join(s.split())