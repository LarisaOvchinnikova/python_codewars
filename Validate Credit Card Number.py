# https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2
def validate(n):
    n = str(n)
    if len(n) % 2 == 0:
        arr = [int(el) * 2 if i % 2 == 0 else int(el) for i,el in enumerate(n)]
    else:
        arr = [int(el) * 2 if i % 2 != 0 else int(el) for i,el in enumerate(n)]
    arr = [sum([int(el) for el in str(elem)]) if elem > 9 else elem for elem in arr]
    return sum(arr) % 10 == 0