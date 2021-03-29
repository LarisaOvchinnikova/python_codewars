# https://www.codewars.com/kata/57096af70dad013aa200007b
def logical_calc(arr, op):
    res = arr[0]
    for i in range(1,len(arr)):
        if op == "AND":
            res = res and arr[i]
        if op == "OR":
            res = res or arr[i]
        if op == "XOR":
            res = res ^ arr[i]
    return res

# 2 case
def logical_calc(arr, op):
    if op == "XOR": op = "^"
    else: op = op.lower()
    return eval((" " + op + " ").join([str(el) for el in arr]))