# https://www.codewars.com/kata/56dbed3a13c2f61ae3000bcd
def noonerize(n):
    return abs(int(str(n[1])[0] + str(n[0])[1:]) - int(str(n[0])[0] + str(n[1])[1:])) if type(n[0]) == int and type(n[1]) == int else "invalid array"