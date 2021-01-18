# https://www.codewars.com/kata/5641275f07335295f10000d0
def split_the_bill(x):
    s = sum(x.values()) / len(x)
    for key in x:
        x[key] = round(x[key] - s, 2)
    return x