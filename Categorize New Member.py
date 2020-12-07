# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
def open_or_senior(data):
    res = []
    for el in data:
        if el[0] >= 55 and el[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")

    return res

# 2 case
def open_or_senior(data):
    return ["Senior" if el[0] >= 55 and el[1] > 7 else "Open" for el in data]