# https://www.codewars.com/kata/53e895e28f9e66a56900011a
def letter_frequency(text):
    t = ''
    for el in text.lower():
        if el.isalpha():
            t +=el
    dct = {letter:t.count(letter) for letter in t}
    return sorted(dct.items(), key=lambda el: (-el[1],el[0]))