https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/python
def find_short(s):
    return min([len(el) for el in s.split(" ")])