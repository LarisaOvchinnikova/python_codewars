https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
def duplicate_encode(word):
    word = word.lower()
    s = ""
    for el in word:
        if word.count(el) == 1:
            s += "("
        else:
            s += ")"
    return s
# ---- 2 case
def duplicate_encode(word):
    word = word.lower()
    return "".join(["(" if word.count(el) == 1 else ")" for el in word])