# https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python
def cookie(x):
    if type(x) == str:
        name = 'Zach'
    elif type(x) == int or type(x) == float:
        name = 'Monica'
    else:
        name = 'the dog'
    return f"Who ate the last cookie? It was {name}!"