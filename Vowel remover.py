https://www.codewars.com/kata/5547929140907378f9000039
def shortcut(s):
    return "".join([el for el in s if el not in "aeuio"])