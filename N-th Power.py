https://www.codewars.com/kata/57d814e4950d8489720008db
def index(array, n):
    try:
        return array[n]**n
    except:
        return -1