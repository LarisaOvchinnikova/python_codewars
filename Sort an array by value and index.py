# https://www.codewars.com/kata/58e0cb3634a3027180000040
def sort_by_value_and_index(arr):
    arr = [(el, el*(i+1)) for i, el in enumerate(arr)]
    arr = sorted(arr, key=lambda x:x[1])
    return [el[0] for el in arr]