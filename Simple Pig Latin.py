https://www.codewars.com/kata/520b9d2ad5c005041100000f/python
def pig_it(text):
    signs = ",.!?"
    lst = text.split(" ")
    res = [el[1:]+el[0]+"ay" if not el in signs else el for el in lst ]
    return " ".join(res)