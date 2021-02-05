# https://www.codewars.com/kata/5808c8eff0ed4210de000008
def part(arr):
    alan = ["Partridge", "PearTree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad"]
    count = 0
    for el in arr:
        if el in alan:
            count += 1
    return "Mine's a Pint" + "!" * count if count > 0 else"Lynn, I've pierced my foot on a spike!!"