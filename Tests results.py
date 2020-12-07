https://www.codewars.com/kata/599db0a227ca9f294b0000c8
def test(r):
    av = round(sum(r) / len(r), 3)
    dct = {
        "h": 0,
        "a": 0,
        "l": 0
    }
    for el in r:
        if el >= 9:
            dct["h"] += 1
        elif el >= 7:
            dct["a"] += 1
        else:
            dct["l"] += 1

    if dct["a"] == 0 and dct["l"] == 0:
        return [av, dct, "They did well"]
    else:
        return [av, dct]