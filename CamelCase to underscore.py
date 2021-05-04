# https://www.codewars.com/kata/5b1956a7803388baae00003a
def toUnderScore(name):
    if name == '': return ''
    t = name[0]
    for i in range(1,len(name)):
        if name[i].isupper() and name[i-1] != '_' :
            t += '_'+ name[i]
        elif name[i-1].isalpha() and name[i].isdigit():
            t += '_' + name[i]
        else:
            t += name[i]
    return t