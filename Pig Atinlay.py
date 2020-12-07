# https://www.codewars.com/kata/58702c0ca44cfc50dc000245/train/python
def pig_latin(word):
    if len(word) <= 3:
        return word
    if word.endswith("ay"):
        word = word[:-2]
        return word[-1] + word[:-1]
    else:
        return word[1:] + word[0] + "ay"