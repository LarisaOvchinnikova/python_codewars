# https://www.codewars.com/kata/56dd927e4c9055f8470013a5
def testit(act, s):
    res = ''
    for i in range(len(act)):
        if act[i] == "run" and s[i] == "_":
            res += '_'
        if act[i] == "run" and s[i] != "_":
            res += '/'
        if act[i] == "jump" and s[i] == "|":
            res += '|'
        if act[i] == "jump" and s[i] != "|":
            res += 'x'
    return res