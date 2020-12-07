https://www.codewars.com/kata/55aea0a123c33fa3400000e7
def sort_me(arr):
    return sorted(arr, key=lambda el:str(el)[-1])