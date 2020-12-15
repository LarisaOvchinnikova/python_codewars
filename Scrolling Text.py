# https://www.codewars.com/kata/5a995c2aba1bb57f660001fd
def scrolling_text(text):
    text = text.upper()
    arr = []
    for i in range(len(text)):
        arr.append(text)
        text = text[1:] + text[0]
    return arr