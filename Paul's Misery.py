# https://www.codewars.com/kata/57ee31c5e77282c24d000024
def paul(x):
    s = 0
    dct = {'kata': 5, 'Petes kata': 10,  'life': 0, 'eating': 1}
    for el in x:
        s += dct[el]
    return 'Super happy!' if s < 40 else 'Happy!' if s < 70 else 'Sad!' if s < 100 else 'Miserable!'