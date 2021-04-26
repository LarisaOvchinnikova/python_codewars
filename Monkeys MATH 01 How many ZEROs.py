# https://www.codewars.com/kata/56c2acc8c44a3ad6e400050a
def countzero(string):
    count = 0
    one =['a','b','d','e','g','o','p','q','0','6','9','D','O','P','Q','R']
    two =['8','%','&','B']
    string = string.replace('()','0')
    return sum([1 if el in one else 2 if el in two else 0 for el in string])