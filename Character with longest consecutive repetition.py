# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python
def longest_repetition(chars):
    if chars == "":
        return ('', 0)
    m = 1
    maxi = m
    s = chars[0]
    for i in range(len(chars)):
        if chars[i] == chars[i-1]:
            m+=1
            if m > maxi:
                maxi = m
                s = chars[i]
        else:
            m = 1
    return (s, maxi)

# 2 case
def longest_repetition(chars):
    if chars == "":
        return '', 0
    s = chars[0]
    for i in range(1, len(chars)):
        if chars[i] == s[-1]:
            s +=chars[i]
        else:
            s += ' '+ chars[i]
    s = s.split()
    m = max([len(el) for el in s])
    x = [el for el in s if len(el) == m]
    return x[0][0], m