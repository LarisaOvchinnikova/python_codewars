# https://www.codewars.com/kata/59126992f9f87fd31600009b
def whoseMove(lastPlayer, win):
    next = 'white' if lastPlayer == 'black' else 'black'
    return lastPlayer if win else next