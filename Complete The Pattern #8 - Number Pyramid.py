https://www.codewars.com/kata/5575ff8c4d9c98bc96000042
def pattern(n):
    s = ''
    s1 = ''
    width = n*2-1
    for i in range(1, n+1):
        if i > 9:
            j = i % 10
        else:
            j = i
        s1 = s1 + str(j)
        s2 = s1 + s1[::-1][1:]
        s = s + s2.center(width)+ '\n'
    return s[:-1]