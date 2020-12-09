# https://www.codewars.com/kata/564ab935de55a747d7000040
def remove(text, what):
    for key in what:
        text = text.replace(key, '', what[key])
    return text