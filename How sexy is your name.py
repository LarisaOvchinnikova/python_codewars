# https://www.codewars.com/kata/571b2ee08d8c9c0d160014ec
def sexy_name(name):
    name = name.replace(' ', '')
    score = sum([SCORES[el.upper()] for el in name])
    if score <= 60: return 'NOT TOO SEXY'
    elif score <= 300: return 'PRETTY SEXY'
    elif score <= 599: return 'VERY SEXY'
    else: return 'THE ULTIMATE SEXIEST'