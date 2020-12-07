https://www.codewars.com/kata/57470efebf81fea166001627
def letter_check(arr):
    arr = [el.lower() for el in arr]
    s1 = set(arr[0])
    s2 = set(arr[1])
    return len(s2-s1) == 0