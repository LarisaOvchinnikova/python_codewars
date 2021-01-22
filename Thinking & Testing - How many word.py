# https://www.codewars.com/kata/56eff1e64794404a720002d2https://www.codewars.com/kata/56eff1e64794404a720002d2
def testit(s):
    s = [el for el in s.lower() if el in "word"]
    count=0
    while "w" in s:
        s = s[s.index("w"):]
        if "o" in s :
            s = s[s.index("o"):]
            if "r" in s:
                s = s[s.index("r"):]
                if "d" in s:
                    s = s[s.index("d"):]
                    count +=1
                else: break
            else: break
        else: break
    return count