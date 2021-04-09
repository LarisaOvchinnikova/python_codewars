# https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2
def solution(pairs):
    arr = ([(str(el[0]), str(el[1])) for el in pairs.items()])
    return ",".join([f"{el[0]} = {el[1]}" for el in sorted(arr)])
