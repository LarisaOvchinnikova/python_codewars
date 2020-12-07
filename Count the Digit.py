# https://www.codewars.com/kata/566fc12495810954b1000030/train/python
def nb_dig(n, d):
    return "".join([str(i**2) for i in range(0, n+1)]).count(str(d))