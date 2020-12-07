# https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036
def toCsvText(arr) :
    res = []
    for i in range(len(arr)):
        s = ",".join([str(el) for el in arr[i]])
        res.append(s)
    return "\n".join(res)

# 2 case
def toCsvText(array) :
    return '\n'.join([','.join([str(el) for el in lst]) for lst in array])