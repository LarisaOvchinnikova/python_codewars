# https://www.codewars.com/kata/5c17b8c93351f6abff000002
def change(text):
    dct = {"zero": "0", "one": "1", "two": "2", "three": "3",
           "four": "4", "five": "5", "six": "6", "seven": "7",
           "eight": "8", "nine": "9"}
    return " ".join([dct[el.lower()] if el.lower() in dct else el for el in text.split()])