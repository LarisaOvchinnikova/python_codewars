#https://www.codewars.com/kata/563319974612f4fa3f0000e0
def square_color(file, rank):
    num = " abcdefgh".index(file)
    return "white" if (num + rank) % 2 == 1 else "black"