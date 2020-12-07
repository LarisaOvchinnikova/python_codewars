https://www.codewars.com/kata/53697be005f803751e0015aa
def encode(st):
    return "".join([char if not char in "aeiou" else str(" aeiou".index(char)) for char in st])


def decode(st):
    return "".join([" aeiou"[int(char)] if char in "12345" else char for char in st])