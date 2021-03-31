# https://www.codewars.com/kata/5697fb83f41965761f000052
def filter_long_words(sentence, n):
    return [el for el in sentence.split() if len(el) > n]