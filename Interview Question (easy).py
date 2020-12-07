https://www.codewars.com/kata/5b358a1e228d316283001892
def get_strings(city):
    obj = {}
    city = list(city.lower().replace(" ", ""))
    s = ''
    for el in city:
        if not el in obj:
            obj[el] = "*"
        else:
            obj[el] += "*"

    for keys  in obj:
        s = s + f"{keys}:{obj[keys]},"
    return s[:-1]