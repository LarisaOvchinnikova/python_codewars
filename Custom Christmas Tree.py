#https://www.codewars.com/kata/5a405ba4e1ce0e1d7800012e
def custom_christmas_tree(chars, n):
    s = ""
    k = 0
    width = n*2-1
    for i in range(1, n+1):
        line = " "*(n-i)
        for j in range(i):
            line = line + chars[k] + " "
            k+=1
            if k == len(chars):
                k = 0
        s = s + line.rstrip() + "\n"
    steam = n // 3
    for i in range (steam):
        if i < steam-1:
            s = s + " "*(n-1) + "|" + "\n"
        else:
            s = s + " "*(n-1) + "|"
    return s