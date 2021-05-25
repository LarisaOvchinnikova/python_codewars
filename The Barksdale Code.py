# https://www.codewars.com/kata/573d498eb90ccf20a000002a
def decode(s):
    dct = {"0": "5", "1": "9", "2": "8", "3": "7", "4": "6",
           "5": "0", "6": "4", "7": "3", "8": "2", "9": "1"}
    return "".join([dct[el] for el in s])