# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def num(s):
  for letter in s:
    if letter.isdigit():
      return letter

def order(s):
  lst = s.split()
  return " ".join(sorted(lst, key=num))


#print(order("is2 Thi1s T4est 3a"))
# ======================================================
print(sorted("he1llo")) # ['1', 'e', 'h', 'l', 'l', 'o']
#2 case:
def order(s):
  lst = s.split()
  return " ".join(sorted(lst, key=lambda x:sorted(x)[0]))


print(order("is2 Thi1s T4est 3a"))