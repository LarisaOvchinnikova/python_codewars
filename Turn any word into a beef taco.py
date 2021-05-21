# https://www.codewars.com/kata/59414b46d040b7b8f7000021
def tacofy(word):
    dct = {'t': 'tomato', 'l': 'lettuce', 'c': 'cheese',
           'g': 'guacamole', 's': 'salsa',
           'a': 'beef', 'o': 'beef','i': 'beef','u': 'beef','e': 'beef'}
    return ['shell'] + ([dct[el] for el in word.lower() if el in dct]) + ['shell']