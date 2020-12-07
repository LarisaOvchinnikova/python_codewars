# https://www.codewars.com/kata/57470efebf81fea166001627
def letter_check(arr):
    s1, s2 = arr[0].lower(), arr[1].lower()
    return len([1 for el in s2 if s1.find(el)!=-1]) == len(s2)