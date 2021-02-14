# https://www.codewars.com/kata/56eff1e64794404a720002d2
def testit(s):
    s = s.lower()
    count = 0
    while "w" in s and "o" in s and "r" in s and "d" in s:
        if "w" in s:
            s = s[s.index("w")+1: ]
        else: break
        if "o" in s:
            s = s[s.index("o")+1: ]
        else: break
        if "r" in s:
            s = s[s.index("r")+1: ]
        else: break
        if "d" in s:
            s = s[s.index("d")+1: ]
        else: break
        count+=1
        print(s)
    return count