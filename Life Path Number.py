https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0
def life_path_number(birthdate):
    y, m, d = map(int, birthdate.split('-'))
    while y >= 10:
        y = sum([int(el) for el in str(y)])
    while int(m) >= 10:
        m = sum([int(el) for el in str(m)])
    while int(d) >= 10:
        d = sum([int(el) for el in str(d)])
    res = y + m + d
    while res >= 10:
        res = sum([int(el) for el in str(res)])
    return res