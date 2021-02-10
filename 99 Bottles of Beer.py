# https://www.codewars.com/kata/52a723508a4d96c6c90005ba
def sing():
    s = 'bottles of beer'
    o = 'on the wall'
    a = []
    for i in range(99, 2, -1):
        a.append(f"{i} {s} {o}, {i} {s}.")
        a.append(f"Take one down and pass it around, {i - 1} {s} {o}.")

    a.append(f"2 {s} {o}, 2 {s}.")
    a.append(f"Take one down and pass it around, 1 bottle of beer {o}.")

    a.append(f"1 bottle of beer {o}, 1 bottle of beer.")
    a.append(f"Take one down and pass it around, no more {s} {o}.")

    a.append(f"No more {s} {o}, no more {s}.")
    a.append(f"Go to the store and buy some more, 99 {s} {o}.")
    return a