https://www.codewars.com/kata/574c5075d27783851800169e
def animals(heads, legs):
    for chickens in range(0, heads+1):
        for cows in range(0, heads+1):
            if cows * 4 + chickens * 2 == legs and cows+chickens == heads:
                return  chickens, cows
    return  "No solutions"