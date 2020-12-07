https://www.codewars.com/kata/568dc69683322417eb00002c
def triple_x(s):
    i = s.find("x")
    return i != -1 and s[i+1:i+3] == "xx"