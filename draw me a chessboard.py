# https://www.codewars.com/kata/56242b89689c35449b000059
def chess_board(rows, columns):
    arr = []
    for i in range(rows):
        s = []
        for j in range(columns):
            if (i + j) % 2 == 0:
                s.append("O")
            else:
                s.append("X")
        arr.append(s)
    return arr