https://www.codewars.com/kata/5f8dd79aa962b600335f7577
def longest_sequence(arr, elem):
    t = "".join([str(el) if str(el) == str(elem) else " " for el in arr])
    return max([len(el)//len(str(elem)) for el in t.split(' ')])