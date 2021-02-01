# https://www.codewars.com/kata/559af787b4b8eac78b000022
def count_me(data):
    if data == "" or not data.isdigit(): return ""
    s = data[0]
    for i in range(1,len(data)):
        if s[-1] != data[i]:
            s += ' ' + data[i]
        else:
            s += data[i]
    return "".join([str(len(el))+el[0] for el in s.split()])