# https://www.codewars.com/kata/57f22b0f1b5432ff09001cab
def well(arr):
    ar = []
    for el in arr:
        ar.extend(el)
    good = len([el for el in ar if type(el) == str and el.lower() == 'good'])
    return 'Fail!' if good == 0 else 'Publish!' if good <= 2 else 'I smell a series!'