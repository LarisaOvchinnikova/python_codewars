# https://www.codewars.com/kata/56f173a35b91399a05000cb7
def find_longest(string):
    return max([len(el) for el in string.split(" ")])