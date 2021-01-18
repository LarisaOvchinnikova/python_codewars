# https://www.codewars.com/kata/58fd9f6213b00172ce0000c9
def split_exp(n):
    arr = []
    n = str(n)
    p = n.find(".")
    x = p-1
    y = len(n) - p
    if p!=-1:
        for i in range(0, p):
            arr.append(n[i]+"0"*x)
            x -= 1
        for i in range(y-1):
            arr.append("."+"0"*i+n[p+1+i])
    else:
        for i in range(len(n)):
            arr.append(n[i]+"0"*(len(n)-i-1))
    arr = [el for el in arr if float(el)!=0]
    return arr