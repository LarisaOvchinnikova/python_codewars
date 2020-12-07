#https://www.codewars.com/kata/5effa412233ac3002a9e471d
def add(num1, num2):
    s1 = str(num1)
    s2 = str(num2)
    l = max(len(s1), len(s2))
    s1 = s1.rjust(l, "0")
    s2 = s2.rjust(l, "0")
    res = ""
    for i in range(l):
        s = int(s1[i]) + int(s2[i])
        res += str(s)
    return int(res)