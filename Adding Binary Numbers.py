https://www.codewars.com/kata/55c11989e13716e35f000013
def add(a,b):
    l = max(len(a), len(b))
    a = a.rjust(l,"0")
    b = b.rjust(l,"0")
    s = ""
    p = 0
    for i in range(l-1, -1, -1):
        el = a[i] + b[i]
        if el == "01" and p == 0:
            s = "1" + s
            p = 0
        elif el == "10" and p == 0:
            s = "1" + s
            p = 0
        elif el == "00" and p == 0:
            s = "0" + s
            p = 0
        elif el == "11" and p == 0:
            s = "0" + s
            p = 1
        elif el == "01" and p == 1:
            s = "0" + s
            p = 1
        elif el == "10" and p == 1:
            s = "0" + s
            p = 1
        elif el == "00" and p == 1:
            s = "1" + s
            p = 0
        elif el == "11" and p == 1:
            s = "1" + s
            p = 1
    if p == 1:
        s = "1" + s
    else:
        s = s.lstrip("0")
    return s if s else "0"

# 2 case
def add(a,b):
    a = [1 if el =="1" else 0 for el in a]
    b = [1 if el =="1" else 0 for el in b]
    n1 = sum([el * 2** (len(a)-i-1) for i,el in enumerate(a)])
    n2 = sum([el * 2** (len(b)-i-1) for i,el in enumerate(b)])
    n = n1 + n2
    s = ''
    while n >= 2:
        last = n % 2
        if last==1:
            s += "1"
        else:
            s+= "0"
        n //=2
    s += "1" if n==1 else "0"
    return s[::-1]