# 6 kyu
# https://www.codewars.com/kata/5848565e273af816fb000449/train/python
def encrypt_this(text):
    words = text.split()
    result = []
    for elem in words:
        word = list(elem)
        word[0] = str(ord(word[0]))
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        result.append(''.join(word))
    return ' '.join(result)