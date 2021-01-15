# https://www.codewars.com/kata/57fb3c839610ce39f7000023
def find(s):
    t = ''
    for el in s:
        if t == '' or t[-1] == el:
            t += el
        else:
            t += " " + el
    t = t.split(' ')
    if len(t) == 1: return ""
    m = len(t[0]) + len(t[1])
    ind = 0
    for i in range(1, len(t)-1):
        if len(t[i]) + len(t[i+1]) > m:
            m = len(t[i]) + len(t[i+1])
            ind = i
    return t[ind]+t[ind+1]