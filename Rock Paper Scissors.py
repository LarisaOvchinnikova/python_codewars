# https://www.codewars.com/kata/5672a98bdbdd995fad00000f
def rps(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if rules[p1] == p2:
        return "Player 1 won!"
    if rules[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

print(rps("Rock", "Paper"))
print(rps("Scissors", "Paper"))
print(rps("Paper", "Paper"))