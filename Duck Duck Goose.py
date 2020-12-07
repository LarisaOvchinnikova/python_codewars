https://www.codewars.com/kata/582e0e592029ea10530009ce
def duck_duck_goose(players, goose):
    n = goose % len(players)
    if n!=0:
        return players[n-1].name
    else:
        return players[-1].name