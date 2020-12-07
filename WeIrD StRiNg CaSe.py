#https://www.codewars.com/kata/52b757663a95b11b3d00062d
def to_weird_case(string):
    s = string.split()
    res = []
    for el in s:
        z = ''
        for i in range(len(el)):
            if i % 2 == 0:
                z += el[i].upper()
            else:
                z += el[i].lower()
        res.append(z)
    return " ".join(res)