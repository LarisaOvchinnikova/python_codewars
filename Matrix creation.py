# https://www.codewars.com/kata/5a34da5dee1aae516d00004a
def get_matrix(n):
    arr = [[0] * n for i in range (n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i][j] = 1
    return arr