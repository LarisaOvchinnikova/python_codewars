#https://www.codewars.com/kata/5432fd1c913a65b28f000342/train/python
def multiplication_table(r,c):
    return [list(range(i, i*c+1, i)) for i in range(1, r+1)]