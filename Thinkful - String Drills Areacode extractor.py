# https://www.codewars.com/kata/585a36b445376cbc22000072
def area_code(text):
    i = text.index('(')
    return text[i+1: i+4]