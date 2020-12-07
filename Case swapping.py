https://www.codewars.com/kata/5590961e6620c0825000008f
def swap(string_):
    s = ""
    for i in string_:
        if i == i.upper():
            s = s + i.lower()
        else:
             s = s + i.upper()
    return s

# ---2 case
def swap(string):
    return string.swapcase()

s = "1"
print(s.isupper())