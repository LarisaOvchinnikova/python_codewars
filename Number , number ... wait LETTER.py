# https://www.codewars.com/kata/5782dd86202c0e43410001f6
def do_math(s) :
    s = s.split( )
    r = []
    for el in s:
        digits = "".join([e for e in el if e.isdigit()])
        letter = "".join([e for e in el if not e.isdigit()])
        r.append((digits, letter))
    r = sorted(r, key=lambda el:el[1])
    num = [el[0] for el in r]
    op = ['+', '-','*','/']
    op = (op * len(num))[:len(num)-1]
    res = num[0]
    for i in range(1,len(num)):
        res = str(eval(res + op[i-1] + num[i]))
    return round(float(res))