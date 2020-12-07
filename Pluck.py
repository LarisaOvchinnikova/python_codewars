# https://www.codewars.com/kata/530017aac7c0f49926000084/train/python
def pluck(objs, name):
    arr = []
    for el in objs:
        if name in el:
            arr.append(el[name])
        else:
            arr.append(None)
    return arr
