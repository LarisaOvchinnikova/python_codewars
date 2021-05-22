# https://www.codewars.com/kata/58381907f8ac48ae070000de/
def is_language_diverse(lst):
    dct = {}
    for el in lst:
        if el['language'] in dct:
            dct[el['language']] += 1
        else:
            dct[el['language']] = 1
    arr = list(dct.values())

    return max(arr) / min(arr) <= 2