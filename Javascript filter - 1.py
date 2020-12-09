# https://www.codewars.com/kata/525d9b1a037b7a9da7000905
def search_names(logins):
    return [el for el in logins if el[0][-1] == "_"]