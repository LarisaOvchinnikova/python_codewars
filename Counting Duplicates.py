# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
def duplicate_count(text):
    text = text.lower()
    lst = [(el,text.count(el)) for el in text]
    s = set(lst)
    l = [el for el in s if el[1]>1]
    return len(l)

print(duplicate_count("indivisibility"))