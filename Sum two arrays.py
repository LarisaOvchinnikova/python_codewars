https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6

def sum_arrays(arr1, arr2):
    if arr1 == [] and arr2 == []:
        return []
    elif arr1 == []:
        return arr2
    elif arr2 == []:
        return arr1
    num1 = int("".join([str(el) for el in arr1]))
    num2 = int("".join([str(el) for el in arr2]))
    s = num1 + num2
    if s >= 0:
        return [int(el) for el in (str(s))]
    else:
        s = -s
        return [-int(el) if i == 0 else int(el) for i, el in (enumerate(str(s)))]
