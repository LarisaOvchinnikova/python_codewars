# https://www.codewars.com/kata/602467452b35dd0021cbf46e
def Hangman(guess, word):
    word = word.lower()
    guess = guess.lower()
    if guess in word:
        i = word.index(guess)
        return "_" * i + guess + "_" * (len(word) - i - 1)
    else:
        return "_" * len(word)
# 2 case
def Hangman(guess, word):
    word = word.lower()
    new_word = [el if guess.lower() == el else '_' for el in word]
    return "".join(new_word)