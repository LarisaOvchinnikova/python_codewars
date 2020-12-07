#https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
def multiplication_table(size):
    return [list(range(i, i*size+1, i)) for i in range(1, size+1)]