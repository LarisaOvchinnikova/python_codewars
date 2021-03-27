# https://www.codewars.com/kata/57efa1a2108d3f73f60000e9
def trim(beard):
    res = []
    for line in beard[:-1]:
        res.append([el.replace("J", "|") for el in line])
    res.append(["..."] * len(beard[-1]))
    return res