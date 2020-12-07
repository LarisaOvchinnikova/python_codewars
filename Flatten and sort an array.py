#https://www.codewars.com/kata/57ee99a16c8df7b02d00045f
def flatten_and_sort(a):
    x = []
    for el in a:
        x.extend(el)
    return sorted(x)