# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def filter_list(l):
  return [el for el in l if str(el).isdigit() and not el == str(el)]

# --- 2 case
def filter_list(l):
  return [el for el in l if not type(el) == str]