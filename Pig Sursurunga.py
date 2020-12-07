https://www.codewars.com/kata/5536aba6e4609cc6a600003d
import re
def sursurungal(txt):
    arr = re.split(r'(\W+)', txt)
    res = []
    i = 0
    while i < len(arr):
        if arr[i].isdigit():
            n = int(arr[i])
            if n in [0,1]:
                res.append(f"{arr[i]} {arr[i+2]}")
            else:
                word = arr[i+2]
                word = word[:-1]
                if n == 2: res.append(f"{n} bu{word}")
                if 3<=n<=9: res.append(f"{n} {word}zo")
                if n>=10: res.append(f"{n} ga{word}ga")
            i+=3
        else:
            res.append(arr[i])
            i+=1
    return "".join(res)