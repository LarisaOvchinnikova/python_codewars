# https://www.codewars.com/kata/57fb0f3f9610ced69000023c

def remove(s):
    for i in range(2):
        t = ''
        for el in s:
            if t == '' or t[-1] == el:
                t += el
            else:
                t += " " + el
        t = t.split(' ')
        s = [el for el in t if len(el) % 2 == 0 or len(el) == 1]
        s = "".join(s)
    return "".join(s)