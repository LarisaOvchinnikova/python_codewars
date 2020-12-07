# https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python
def capitalize(s):
    s1 = "".join([el.upper() if i % 2 == 0 else el.lower() for i, el in enumerate(s)])
    s2 = "".join([el.upper() if i % 2 != 0 else el.lower() for i, el in enumerate(s)])
    return [s1, s2]