https://www.codewars.com/kata/5864614683f7e6e7830000c1
def bite(thing):
    if "race" in thing:
        if thing["race"] == "human":
            thing["race"] = "zombie"
    return thing