https://www.codewars.com/kata/5264d2b162488dc400000001
def spin_words(s):
    arr = s.split(" ")
    lst = [word[::-1] if len(word) >= 5 else word for word in arr ]
    return " ".join(lst)