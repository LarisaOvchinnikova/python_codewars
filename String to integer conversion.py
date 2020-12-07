https://www.codewars.com/kata/54fdadc8762e2e51e400032c
def my_parse_int(s):
    s = s.strip()
    lst = [el for el in s if not el.isdigit()]
    return "NaN" if len(lst) > 0 else int(s)