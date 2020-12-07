# https://www.codewars.com/kata/583989556754d6f4c700018e/train/python
def multiples(s1,s2,s3):
    return [el for el in range(1, s3) if el % s1 == 0 and el % s2 == 0]