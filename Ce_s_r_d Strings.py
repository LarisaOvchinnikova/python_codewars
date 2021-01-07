https://www.codewars.com/kata/5ff6060ed14f4100106d8e6f
def uncensor(infected, discovered):
    s = ""
    for el in infected:
        if el == "*":
            s += discovered[0]
            discovered = discovered[1:]
        else:
            s += el
    return s