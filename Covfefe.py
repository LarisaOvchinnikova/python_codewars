# https://www.codewars.com/kata/592fd8f752ee71ac7e00008a
def covfefe(s):
    return s.replace("coverage", "covfefe") if "coverage" in s else s + " covfefe"