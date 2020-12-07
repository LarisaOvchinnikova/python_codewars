# https://www.codewars.com/kata/5a145ab08ba9148dd6000094
def doubles(s):
    arr = [s[0]]
    for i in range(1, len(s)):
        if arr == [] or s[i] != arr[-1]:
            arr.append(s[i])
        else:
            arr.pop()
    return "".join(arr)