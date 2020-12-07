https://www.codewars.com/kata/5533c2a50c4fea6832000101
def createDict(keys, values):
    dct = {}
    while len(keys) > len(values):
        values.append(None)
    for i, key in enumerate(keys):
        dct[key] = values[i]
    return dct

print(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]))

# --- 2 case
def createDict(keys, values):
    dct = dict(zip(keys, values))
    if len(keys) > len(values):
        dif = len(keys) - len(values)
        for el in keys[-dif:]:
            dct[el] = None

    return dct
