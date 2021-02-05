# https://www.codewars.com/kata/580a41b6d6df740d6100030c/
def alan(arr):
    s = ['Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway']
    count = 0
    for el in set(arr):
        if el in s:
            count+=1
    return 'Smell my cheese you mother!' if count == 4 else 'No, seriously, run. You will miss it.'