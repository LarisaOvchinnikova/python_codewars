# https://www.codewars.com/kata/59bd84b8a0640e7c49002398
def t_area(s):
    a = [el.count(' ') for el in s.split('\n') if el !='']
    return (len(a)-1) * max(a) / 2