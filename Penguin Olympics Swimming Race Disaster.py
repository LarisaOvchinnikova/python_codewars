# https://www.codewars.com/kata/6022c97dac16b0001c0e7ccc
def calculate_winners(snapshot, penguins):
    waves = ([el.replace("~","--") for el in (snapshot.lower().split("\n"))])
    w = sorted([(len(el) - el.find("p"), penguins[i]) for i,el in enumerate(waves)], key=lambda el:el[0])[:3]
    w = [(i+1, el[1]) for i, el in enumerate(w)]
    medals = {1: "GOLD", 2: "SILVER", 3: "BRONZE"}
    return ", ".join([f"{medals[el[0]]}: {el[1]}" for el in w])