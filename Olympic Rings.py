# https://www.codewars.com/kata/57d06663eca260fe630001cc
def olympic_ring(s):
    one = 'AabdgeopqDOPRQ'
    two = 'B'
    count = 0
    for el in s:
        if el in one:
            count += 1
        if el in two:
            count += 2
    count //=2
    return 'Not even a medal!' if count <= 1 else  'Bronze!' if count == 2 else 'Silver!' if count == 3 else 'Gold!'