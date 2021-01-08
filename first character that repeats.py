# https://www.codewars.com/kata/54f9f4d7c41722304e000bbb
def first_dup(s):
    for el in s:
        if s.count(el) > 1:
            return el
    return None