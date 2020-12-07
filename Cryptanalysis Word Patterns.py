# https://www.codewars.com/kata/5f3142b3a28d9b002ef58f5e/train/python
def word_pattern(word):
    word = word.lower()
    obj = {}
    x = 0
    for letter in word:
        if not letter in obj:
            obj[letter] = x
            x+=1
    return ".".join([f"{obj[el]}" for el in word])