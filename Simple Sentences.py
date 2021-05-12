# https://www.codewars.com/kata/5297bf69649be865e6000922
def make_sentences(parts):
    return (' '.join(parts)).replace(' .','.').replace(' ,',',').rstrip('.') + '.'