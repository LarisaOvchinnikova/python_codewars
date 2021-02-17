# https://www.codewars.com/kata/56b8903933dbe5831e000c76
def spoonerize(words):
    words = words.split(" ")
    return words[1][0] + words[0][1:] + " " + words[0][0] + words[1][1:]