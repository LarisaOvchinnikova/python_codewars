# https://www.codewars.com/kata/5fc4349ddb878a0017838d0f
def red_knight(N, P):
    return ('White' if P % 2 == N else 'Black', P * 2)