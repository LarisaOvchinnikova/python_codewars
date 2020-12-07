https://www.codewars.com/kata/598d91785d4ce3ec4f000018
def name_value(lst):
    alph = ' abcdefghijklmnopqrstuvwxyz'
    return [sum([alph.index(letter) for letter in word]) * (i+1) for i,word in enumerate(lst)]