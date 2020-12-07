# https://www.codewars.com/kata/53af2b8861023f1d88000832
def areYouPlayingBanjo(name):
    if name[0] == "r" or name[0] == "R" :
        return f"{name} plays banjo"
    else:
        return F"{name} does not play banjo"