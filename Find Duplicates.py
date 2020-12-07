https://www.codewars.com/kata/5558cc216a7a231ac9000022
def duplicates(array):
    arr = [el for i,el in enumerate(array) if array.count(el) > 1 and i!= array.index(el) ]
    return [el for i,el in enumerate(arr) if i == arr.index(el)]
