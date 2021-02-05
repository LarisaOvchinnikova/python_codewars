# https://www.codewars.com/kata/588805ca44c7e8c3a100013c
def different_squares(m):
    arr = []
    w = len(m[0])
    for i in range(len(m)-1):
        for j in range(w-1):
            a = (m[i][j], m[i][j+1], m[i+1][j], m[i+1][j+1])
            arr.append(a)
    return len(set(arr))