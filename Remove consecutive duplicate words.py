https://www.codewars.com/kata/5b39e91ee7a2c103300018b3
def remove_consecutive_duplicates(s):
    s = s.split()
    arr = []
    for i in range(len(s)):
        if arr == [] or s[i] != arr[-1]:
            arr.append(s[i])
    return " ".join(arr)