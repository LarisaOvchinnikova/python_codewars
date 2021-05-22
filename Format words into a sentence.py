# https://www.codewars.com/kata/51689e27fe9a00b126000004
def format_words(words):
    if words == [] or words == None: return ""
    s = [el for el in words if el != ""]
    if len(s)> 1:
        return ", ".join(s[:-1]) + " and " + s[-1]
    else:
        return "".join(s)