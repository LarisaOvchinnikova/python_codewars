https://www.codewars.com/kata/59564f3bcc15b5591a00004a
def filter_even_length_words(words):
    return [el for el in words if len(el) % 2 == 0]