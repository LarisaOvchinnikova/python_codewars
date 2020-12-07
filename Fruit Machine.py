# https://www.codewars.com/kata/590adadea658017d90000039

def fruit(reels, spins):
    score = ['','Jack', 'Queen', 'King', 'Bar', 'Cherry', 'Seven', 'Shell', 'Bell', 'Star', 'Wild']
    attempt = [reels[0][spins[0]], reels[1][spins[1]], reels[2][spins[2]] ]
    dct = {el:attempt.count(el) for el in attempt}
    s = 0
    for key in dct:
        if dct[key] == 2:
            if "Wild" in dct and key !="Wild":
                s = s + score.index(key) * 2
            else:
                s = s + score.index(key)
        elif dct[key] == 3:
            s = s + score.index(key) * 10
    return s