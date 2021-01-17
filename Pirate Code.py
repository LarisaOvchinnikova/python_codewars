# https://www.codewars.com/kata/59e77930233243a7b7000026
def amaro_plan(pirate_num):
    gold = pirate_num * 20
    amaro = gold - (pirate_num - 1) // 2
    res = [amaro]
    for i in range(pirate_num - 1):
        res.append(0) if i % 2 == 0 else res.append(1)
    return res