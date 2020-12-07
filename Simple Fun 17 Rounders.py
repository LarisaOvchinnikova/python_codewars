# https://www.codewars.com/kata/58846d50f54f021d90000012
def rounders(value):
    value = list(str(value))
    value = [int(el) for el in value]
    for i in range(len(value)-1, 0, -1):
        if value[i] >= 5:
            value[i-1] += 1
        value[i] = 0
    return int("".join(list(map(str,value))))