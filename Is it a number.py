https://www.codewars.com/kata/57126304cdbf63c6770012bd
def isDigit(s):
    try:
        s = float(s)
        return True
    except:
        return False