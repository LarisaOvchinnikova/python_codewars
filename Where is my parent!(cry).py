# https://www.codewars.com/kata/58539230879867a8cd00011c
def find_children(s):
    if s == "" : return ""
    s = sorted(s.lower())
    t = ''
    for el in s:
        if t =='' or t[-1] == el:
            t += el
        else:
            t += " "+ el
    return t.title().replace(' ', '')

# 2 case
def find_children(dancing_brigade):
    return ''.join(sorted(dancing_brigade, key=lambda el:(el.upper(), el.islower())))


# 3 case
def find_children(d):
    return ''.join(sorted({(c*d.lower().count(c)).title() for c in d.lower()}))