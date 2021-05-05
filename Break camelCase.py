def solution(s):
    t = ''
    for i in range(len(s) - 1):
        if s[i].islower() and s[i+1].isupper():
            t += s[i] + ' '
        else:
            t += s[i]
    return t + s[-1]