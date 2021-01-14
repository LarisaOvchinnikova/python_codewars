# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed
def replace_exclamation(s):
    t = ''
    for el in s:
        if el.lower() in "aeuio":
            t +="!"
        else:
            t += el
    return t