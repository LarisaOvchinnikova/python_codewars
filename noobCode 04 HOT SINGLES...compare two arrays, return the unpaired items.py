# https://www.codewars.com/kata/57475353facb0e7431000651
def hot_singles(arr1, arr2):
    a1 = [el for el in arr1 if el not in arr2]
    a2 = [el for el in arr2 if el not in arr1]
    res = a1 + a2
    return [el for i, el in enumerate(res) if i == res.index(el)]