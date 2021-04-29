# https://www.codewars.com/kata/5b049d57de4c7f6a6c0001d7
def apparently(string):
    s = string.split(' ')
    if s[-1] == "and":
        s[-1] = 'and apparently'
    if s[-1] == "but":
        s[-1] = 'but apparently'
    for i in range(len(s)-1):
        if s[i] == 'and' and s[i+1]!= "apparently":
            s [i] = 'and apparently'
        if s[i] == 'but' and s[i+1]!= "apparently":
            s [i] = 'but apparently'
    return " ".join(s)