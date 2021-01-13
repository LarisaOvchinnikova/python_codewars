# https://www.codewars.com/kata/57fafb6d2b5314c839000195
def remove(s):
    return " ".join([el for el in s.split(" ") if el.count("!") != 1])