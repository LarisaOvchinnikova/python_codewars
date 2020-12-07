https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca


def solve(arr):
    dir = [el.split()[0] for el in arr]
    street = [" ".join(el.split()[1:]) for el in arr][::-1]
    reversed_dir = dir[::-1][:-1]
    rev = ["Begin"] + ["Left" if el == "Right" else "Right" for el in reversed_dir]
    return [f"{rev[i]} {street[i]}" for i in range(len(rev))]
