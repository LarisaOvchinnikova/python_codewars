# https://www.codewars.com/kata/58291fea7ff3f640980000f9
def all_continents(lst):
    continents = {}
    for el in lst:
        if el['continent'] in continents:
            continents[el['continent']] += 1
        else:
            continents[el['continent']] = 1
    return len(continents) == 5