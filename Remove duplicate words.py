https://www.codewars.com/kata/5b39e3772ae7545f650000fc
def remove_duplicate_words(s):
    arr = s.split(" ")
    res = []
    for el in arr:
        if not el in res:
            res.append(el)
    return " ".join(res)