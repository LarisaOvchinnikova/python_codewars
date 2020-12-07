# https://www.codewars.com/kata/558fa34727c2d274c10000ae/train/python

def scrabble_score(st):
  st = st.replace(" ", "").upper()
  return sum([dict_scores[el] for el in st])