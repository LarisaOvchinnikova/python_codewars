https://www.codewars.com/kata/57fd696e26b06857eb0011e7/solutions/python
def dative(word):
    front = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
    back = ['a', 'á', 'o', 'ó', 'u', 'ú']
    vowels = [el for el in word if el in front or el in back]
    first = vowels[0]
    last = vowels[-1]
    if last in back:
        return word+"nak"
    elif first in front:
        return word+"nek"