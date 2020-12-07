# https://www.codewars.com/kata/5202ef17a402dd033c000009
def title_case(title, minor_words=''):
    words = title.split()
    if title == "": return ""
    return title[0].upper() + " ".join([el.title() if el.lower() not in minor_words.lower().split() else el.lower() for el in words])[1:]